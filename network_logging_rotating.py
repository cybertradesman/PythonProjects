import logging
from logging.handlers import RotatingFileHandler
from netmiko import ConnectHandler

logger = logging.getLogger("networkLogger") 

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = RotatingFileHandler( 
    "network_automation.log", maxBytes=200 * 1024, backupCount=3  # Realistic: 200KB
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(
    logging.Formatter(  # Fixed: logging.Formatter()
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
)

console_handler.setFormatter(file_handler.formatter)  # Reuse
logger.addHandler(console_handler)
logger.addHandler(file_handler)


device = {
    "device_type": "cisco_ios",  # Matches whichever router, list of device type names available online
    "host": "192.168.2.1",  # whichever IP is assigned for management of the particular network device (ipv4 or ipv6)
    "port": 22,  # SSH (VTY setup)
    "username": "username",  
    "password": "password",    
}
command = "show ip interface brief"
# IMPORTANT MONOLOGUE (to reader):
# The possible commands to send are endless- imagine this whole program in a loop, allowing for endless possibilities- configuration alteration on a massive scale,
# new deployments of updates, checks for security (config hasn't changed unauthorized), SOC Analyst/Incident Response(IR) Work, and Cybersecurity Governance/RMF protocols.
# I WILL expand on this program much further with network instrumentation & orchestration with Ansible/Python. I could use various forms of data collected across many devices,
# or on specific ports to make data visualizaitons in R, i.e. these could include network performance statistics related to SOC Analyst L1 work, i.e.
# categories of data in DSCP bits (pie charts and more can be generated with R!), Calculus to check for continuity/discontinuity with IVT, Newton's Method, Bisection Method, derivatives, limits...
# and to explain the continuity thing, it's about finding possible coefficients in the calculus of network flow (i.e. runts,shorts,input/output errors, bandwidth, latency) that
# would best run on this network for these users with the problem (resolving a slow connection ticket)- metrics of minimal ideal performance so that sources of interference were removed 
# without damaging overall network quality for others too much (Which router or switch number in which room from what IDF around what appliances? Cost Benefit Analysis needs to know, the risk management/governance people)
# On router configurations, priority bits for different data that would need to be re-prioritized/routed differently can be used to sort out info with the Logger/Connect Handler library too
# Certain performance statistics could be altered to reflect approved, positive changes for the network infrastructure. This can include UFM, firewalls, and L2/L3 device setups (depending on protocol)...
# Sources of interference could be mapped out in R and handly compiled, reported, and email automatically to the SOC L1 responsible for keeping an eye on it (Anomaly Detection)
# Examples^: too much data being allowed in the video end but minimal in the text-based data side (could be users streaming 4k all the dang time on a 500mbps network, or a potential UDP video stream DDoS Attack)
# ...whatever the case, speedy and frugal actions can be made with Automation & Machine Learning (ML) algorithms, constantly updating code and people to find what the latest issues are.
print(
    f"Testing: {device['host']} - Expect {'auth fail' if 'wrong' in device['username'] else 'conn fail'}"
)
try:
    logger.info(f"Connecting to {device['host']}")
    net_connect = ConnectHandler(**device)
    logger.info(f"Sending: {command}")
    output = net_connect.send_command(command)
    net_connect.disconnect()
    filename = f"{command.replace(' ', '_')}_{device['host']}.csv"
    with open(filename, "w") as f:
        f.write(output)
    logger.info(f"Output saved to {filename}")
except Exception as e:
    logger.error(f"Failed: {str(e)}")
    logger.exception("Connection Failed")