#Make HTML Page 


def main():
    body = "Stay tuned for our amazing summer sale!"
    createHTML(body)

def createHTML(body):
    file = open('drill.html','w')
    
    template = """
    <html>
    <body>
    {}
    </body>
    </html>""".format(body)

    file.write(template)
    file.close()

if __name__ == "__main__": main()

