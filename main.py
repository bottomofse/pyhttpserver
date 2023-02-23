from server.server import BaseServer

def main():
    server = BaseServer('localhost', 8000)
    server.start_listen()

if __name__ == '__main__':
    main()
