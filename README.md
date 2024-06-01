## **How to run?**
```
git clone https://github.com/AGHRapidPro/DiscordPinger
cd DiscordPinger
pip install -r requirements.txt
python3 main.py "discord_webhook_url" "1.2.3.4" "192.168.1.1" "etc."
```
^Make sure to separate arguments using spaces.


You must provide at least two arguments - discord webhook url and an ip address.
Not tested with IPv6.

## **How to build a docker image?**
Example:
```
git clone https://github.com/AGHRapidPro/DiscordPinger
cd DiscordPinger
docker buildx build -t aghrapidpro/discord-pinger:1.1 -t aghrapidpro/discord-pinger:latest --platform linux/386,linux/amd64,linux/arm,linux/arm64,linux/ppc64le,linux/s390x --push .
```

## **How to run as a docker container?**
Example:
```
docker run -itd aghrapidpro/discord-pinger:latest https://discord.com/api/webhooks/1234567890/oqlGOtDn9JDe30 192.168.1.1 192.168.1.2
```
## **How to run using docker-compose.yaml?**
example file:
https://github.com/AGHRapidPro/DiscordPinger/blob/main/docker-compose.yaml
