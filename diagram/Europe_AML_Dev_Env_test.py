from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import AKS, AppServices, FunctionApps
from diagrams.azure.database import SQLServers
from diagrams.azure.network import VirtualNetworks
from diagrams.azure.devops import Devops
from diagrams.azure.identity import ActiveDirectory
from diagrams.azure.integration import ServiceBus
from diagrams.azure.security import KeyVaults
from diagrams.azure.general import Subscriptions, Allresources, Monitor
from diagrams.onprem.compute import Server
from diagrams.generic.cartoon import Mario

with Diagram("UBO Development Environment", show=False):
    directory = ActiveDirectory("Volvo AD")
    
    with Cluster("Virtual Network"):
        container = AKS("Kubernetes Cluster")
        queue = ServiceBus("queue")
        keyv = KeyVaults("AML KeyVault")
        aml_subscription = Subscriptions("AML Azure Subscription")
        monitor_agent = Monitor("monitor_agent")
        mymario = Mario("mymario")
        
        with Cluster("ubo_module"):
            ubo_module_app = [AppServices("UBO App1"),AppServices("UBO App2")]
        ubo_module_db = SQLServers("UBO Database")
        ubo_module_func = FunctionApps("UBO Module Function")

    
    devops = Devops("Dev/Ops")
    vfs_connect_appsrv = Server("VFS Connect Application Server")

    vfs_connect_appsrv >> queue >> ubo_module_app >> ubo_module_db
    ubo_module_func >> ubo_module_app
    container >> Edge(label="RBAC") >> directory
    devops >> directory


