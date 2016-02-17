import json


class MsgFormater:
    """
        Formating messages

        {
            type;
            sender;

            datas;
            comments;
        }
    """
    def __init__(self, ip, port): #int, int
        self.ip = ip
        self.port = port


    def print_msg1(self):
        data = {}
        data["sender_ip"] = self.ip
        data["sender_port"] = self.port
        json_data = json.dumps(data)
        print(json_data)
        print(type(json_data))



def main():
    test1 = MsgFormater(100, 200)
    test1.print_msg1()



if __name__ == "__main__":
    main()
