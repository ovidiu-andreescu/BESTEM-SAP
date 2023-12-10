from db_config.config import Session
from db_config.models import ProductCluster
from sqlalchemy import func

session = Session()

subquery = (session.query(ProductCluster.cluster_id, ProductCluster.customer_id, func.count().label('product_count'))
            .group_by(ProductCluster.cluster_id, ProductCluster.customer_id)
            .subquery())

query = (session.query(subquery.c.customer_id, subquery.c.cluster_id, subquery.c.product_count)
         .order_by(subquery.c.customer_id, subquery.c.cluster_id))

results = query.all()