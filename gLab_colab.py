import requests, os                                  
# Download and Install ffuf in google-colab
url = """https://github.com/ffuf/ffuf/releases/download/v1.3.1/ffuf_1.3.1_linux_amd64.tar.gz"""
with open(url.split('/')[-1], "wb+") as f:
    f.write(requests.Session().get(url).content)
os.system('tar -xvzf ffuf*.tar.gz && rm CHANGELOG.md LICENSE README.md ffuf*.tar.gz && mv ffuf /bin')


# Download and Install ngrok in google-colab
os.system('curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok')

# Install other packages
os.system("""
apt-get install nano file zip git poppler-utils php net-tools tar && pip install speedtest-cli wordlist
""")
