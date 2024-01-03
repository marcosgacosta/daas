from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.aws.network import CF


with Diagram("MomoTech.us Architecture", show=False):

     with Cluster("AWS"):
        dns = Route53("DNS")
        lb = ELB("AppLoadBalancer")
        cf = CF("CloudFront")

        with Cluster ("MomoTech website"):
            s3 = S3("momotech.us")
            with Cluster("PrivateSubnet"):
                webapp = [EC2("webapp")]


        dns >> lb >> webapp
        dns >> cf >> s3
