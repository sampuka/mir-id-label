class labeldata:
    name = "Robot name"
    pic = "default-pic.jpg"
    mir_type = "MIRTYPE"
    mir_id = "MIR_DEFAULT"
    ip = "IP address"
    wifi = "WiFi name"

    def __init__(self, name_, pic_, mir_type_, mir_id_, ip_, wifi_):
        self.name = name_
        self.pic = pic_
        self.mir_type = mir_type_
        self.mir_id = mir_id_
        self.ip = ip_
        self.wifi = wifi_

labels = [
    labeldata("Gazellen", "gazelle.jpg", "MIR250", "Gazellen", "10.52.180.105", "MIR_204703014"),
    labeldata("Pumba", "pumba.jpg", "MIR600", "Pumba", "10.52.180.180", "?"),
    labeldata("Malik", "malik.jpg", "MIR100", "Malik - MIR100", "10.52.180.104", "?"),
    labeldata("Rhino", "rhino.jpg", "MIR1350", "EMB 1350CC", "10.52.180.183", "?")
]

