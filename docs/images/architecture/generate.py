from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.programming.framework import Angular

with Diagram("LEO-IOT", show=False, direction='TB'):
    with Cluster("vm139"):
        leo_backend = Custom("Backend", "quarkus-logo.jpg")
        with Cluster("Frontend"):
            leo_frontend = Angular("Frontend")
            model = Custom("3d Model", "three-js-logo.png")
            dashboard = Custom("Dashboard", "dashboard-icon.webp")
            graphana = Custom("Graphana", "grafana_logo.png")
            leo_frontend << Edge(label="Part of") << model
            leo_frontend << Edge(label="Part of") << dashboard << Edge(label="Supplies Dashboard with Graphs") << graphana
        leo_frontend >> Edge(label="Calls Api") >> leo_backend
        timescale = Custom("Database", "timescale_logo.png")
        leo_backend >> Edge(label="persists sensor data and retrieves it") >> timescale


    with Cluster("Value-Sim"):
        leo_sim = Custom("Value Simulator", "quarkus-logo.jpg")
        postgres = Custom("Database", "postgres_logo.png")
        leo_sim >> Edge(label="Stores Config") >> postgres

    with Cluster("vm90"):
        mosquitto = Custom("Mqtt-Broker", "mosquitto_logo.png")

    with Cluster("5AHIF"):
        leobox1 = Custom("LeoBox", "leobox.png")

    with Cluster("4BHITM"):
        leobox2 = Custom("LeoBox", "leobox.png")

    leobox1 >> Edge(label="sends sensor data") >> mosquitto
    leobox2 >> Edge(label="sends sensor data") >> mosquitto

    mosquitto >> Edge(label="subscribe to sensor data") >> leo_frontend
    mosquitto >> Edge(label="subscribe to sensor data") >> leo_backend

    leo_sim >> Edge(label="sends fake sensor data") >> mosquitto


