from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=True):
    ELB("lb") >> EC2("web1") >> RDS("userdb")
    ELB("lb") >> EC2("web2") >> RDS("userdb")