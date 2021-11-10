#Import Jinja2 and PyYAML
from jinja2 import Environment,FileSystemLoader #Jinja work with template and python,is supermega useful 4 NetworkAutomation
import yaml
#declare template enviroment
ENV = Environment(loader=FileSystemLoader('.'))

def get_interface_speed(interface_name):
    """
    get interafce_speed returns the default Mbps value for a given network interface by looking for certain keywords in the name


    Add speed {{interface.name|get_interface_speed}} to temmplate after {%endif%}
    """
    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100
# class NetworkInterface(object):
#     def __init__(self,name,description,vlan,uplink=False):
#         self.name = name
#         self.description = description
#         self.vlan = vlan
#         self.uplink = uplink
#
# #interface_obj = NetworkInterface("GigabitEthernet0/1","Server Port",10)
#ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("template.j2")

with open("data.yml") as f:
    interfaces = yaml.safe_load(f)
    print(template.render(interface_list=interfaces))
