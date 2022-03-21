class labeldata:
    name = "Robot name"
    pic = "default-pic.jpg"
    mir_type = "MIRTYPE"
    mir_id = "MIR_DEFAULT"
    wifi = "WiFi name"

    def __init__(self, name_, pic_, mir_type_, mir_id_, wifi_):
        self.name = name_
        self.pic = pic_
        self.mir_type = mir_type_
        self.mir_id = mir_id_
        self.wifi = wifi_

labels = [
    labeldata("Christina", "unnamed.jpg", "MIR250", "PS-004", "PS-004"),
#    labeldata("Unnamed", "unnamed.jpg", "MIR600", "Red Dragon Proto 1", "?"),
    labeldata("Malik", "malik.jpg", "MIR100", "Malik - MIR100", "?"),
    labeldata("Gazellen", "gazelle.jpg", "MIR250", "Gazellen", "MIR_204703014"),
    labeldata("Unnamed", "unnamed.jpg", "MIR200", "MiR_S1184", "MIR_S1184"),
    labeldata("Unnamed", "unnamed.jpg", "MIR500", "MiR_U0156", "?"),
    labeldata("Pumba", "pumba.jpg", "MIR600", "Pumba", "?"),
    labeldata("Nora", "nora.jpg", "MIR250", "PS16 - Nora", "PS-016"),
    labeldata("Yeti", "yeti.jpg", "MIR600", "Yeti - KCH", "?"),
    labeldata("Næsehornet", "rhino.jpg", "MIR1350", "EMB 1350CC", "?"),
    labeldata("Unnamed", "unnamed.jpg", "MIR200", "MIR_201903133", "MIR_201903133"),
    labeldata("Unnamed", "unnamed.jpg", "MIR200", "MiR_S1033", "MiR_AGV7")
]

