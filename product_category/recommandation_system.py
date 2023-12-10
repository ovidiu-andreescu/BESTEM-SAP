from db_config.config import Session
from db_config.models import ProductCluster
from sqlalchemy import func


def recommend():
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
                   .all()
                   )

    for cluster_id, customer_id, total_product_count in max_cluster:
        print(f"Cluster ID: {cluster_id}, Customer ID: {customer_id}, Max CLuster customer: {total_product_count}")

    return max_cluster