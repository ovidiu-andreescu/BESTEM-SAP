from db_config.config import Session
from db_config.models import ProductCluster
from sqlalchemy import func, and_
import random

def recommend_products():
    session = Session()

    subquery = (session.query(
        ProductCluster.cluster_id,
        ProductCluster.Customer_ID,
        func.count().label('product_count')
    )
    .group_by(ProductCluster.cluster_id, ProductCluster.Customer_ID)
    .subquery())

    sum_query = (session.query(
        subquery.c.cluster_id,
        subquery.c.Customer_ID,
        func.sum(subquery.c.product_count).label('total_product_count')
    )
    .group_by(subquery.c.cluster_id, subquery.c.Customer_ID)
    .order_by(subquery.c.Customer_ID)
    .subquery())

    max_cluster = (session.query(
        sum_query.c.cluster_id,
        sum_query.c.Customer_ID,
        func.max(sum_query.c.total_product_count).label('max_cluster_customer')
    )
    .group_by(sum_query.c.cluster_id, sum_query.c.Customer_ID)
    .all())

    product_recommendations = []

    for cluster_id, top_customer_id, _ in max_cluster:
        all_products = session.query(ProductCluster.Product_ID).filter(
            ProductCluster.cluster_id == cluster_id
        ).all()

        top_customer_products = session.query(ProductCluster.Product_ID).filter(
            and_(
                ProductCluster.cluster_id == cluster_id,
                ProductCluster.Customer_ID == top_customer_id
            )
        ).all()

        recommended_products = list(set(all_products) - set(top_customer_products))
        if recommended_products:
            recommended_product = random.choice(recommended_products)
            product_recommendations.append((cluster_id, top_customer_id, recommended_product))

    for cluster_id, customer_id, product in product_recommendations:
        print(f"Cluster ID: {cluster_id}, Customer ID: {customer_id}, Recommended Product: {product}")

    return product_recommendations
