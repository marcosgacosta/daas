# Diagrams as a Code (DaaS)
Since everything is "as a code" these days, this is an attempt to make Diagrams as a Code. Of course, the potential it's not in writing directly but with the integration with other products, for example, if you train an LLM to code using this, or maybe you could read a terraform state or config file and generate a diagram from that. 

If you really want to see some awesome diagrams, check the repo [Diagrams as a Code](https://github.com/HariSekhon/Diagrams-as-Code) from HariSekhon.

For my website Momotech.us I run a really simple architecture, maybe simpler than it should be if we measure it by any best practices including the AWS Well-Architected Framework, but we are here to talk about Diagrams.
So, I use Route53 for DNS, and then, I host a static website using S3, and a web app for my resume chatbot that runs on an EC2 instance behind an Elastic Load Balancer.

So, if you install Graphviz and the diagrams package [(instructions here)](https://github.com/mingrammer/diagrams) you could write the following code:


```
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.aws.network import CF


with Diagram("Resume ChatBot", show=False):
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
```

And get the following diagram:


