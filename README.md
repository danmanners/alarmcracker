# Alarm Cracker

I managed to lock myself out of my [Caddx/NetworX/GE NX-595E](https://www.interlogix.com/intrusion/product/networx-ip-communication-module) alarm panel web interface. So I decided to write a quick script to brute force my way back in.

I knew that I had NOT changed the primary username from `installer`, and I was reasonably sure that the code was 4 digits. This was a quick way to brute force it.

Fun fact: the default login is `u: installer / p: 9713`. That turned out to be **EXACTLY** what mine was set to. If you haven't tried that first, do that.

That being said, here's how you might run this if you have changed the pin code, or password.

## Setting up and Running Alarm Cracker

You'll need to change at least one of the following three variables in the script:

```python
# Variables
username = "installer"
ipaddr = "10.5.104.150"
charNumbers = 4
```

You'll need to set the IP Address for your panel. If necessary, change the username and the number of characters that the PIN may be. Hopefully, it's still 4 characters, as 10,000 PIN Codes will take roughly 1h 20m, or ~125 attempts/minute, as much faster than that starts erroring out as the board believes you to be DDOS'ing it.

Once you update the values and have saved the file, you can set up your environment with:

```shell
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r req.txt
```

Once the environment is configured, run the script with:

```shell
$ ./alarmcracker.py
```

This will take roughly 80-90 minutes to complete, if your code is `9999`.

Good luck, and make sure you write your code down next time!