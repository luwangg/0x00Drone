# 0x00Drone
A modification to the DJI Mavic Pro used for hacking from the sky and to drop physical backdoors, licensed under GNU GPLv3

# CURRENT STATUS: PROTOTYPE DEVELOPMENT
---

# What is the 0x00Drone?
The 0x00Drone is a joint effort between three core members of 0x00sec to weaponize a drone for hacking purposes, in the name of 0x00sec. Now this has already been done before by some people, but what sets us apart from the others is that we want to make the 0x00Drone as compact and stealthy as possible, specially designed for red teamers and covert-ops on big companies. The 0x00Drone uses the [DJI Mavic pro](https://www.dji.com/products/mavic) as our drone. It features:

* A long flight time. According to my estimates, with our "package" attached to the drone, the flight time will be no less than 15-20 minutes
* The drone has a long range, from 5 to 7 km!
* The drone has a high resolution camera for all your physical recon needs.
* The drone is capable of following a human being, perfect for tracking individuals.
* But the most important feature why we choose to mod this drone is because **both drones can be folded to the size of a water bottle!** This allows for low-profile attacks because you can just put the drone in one pocket and our hacking package in another pocket. You can walk close to any facility without looking suspicious (unlike other weaponized drones that are a big red flag because you can't put them away easily). Then when you are close enough you hide, unfolde the drone, attach the 0x00Drone package to it, and take off!
* Another reason why we have chosen this drone is because **we already have firmware samples available for it that are ready to be modded**. That's right, we may or may not write custom firmware for the drone.

The only con to this drone is that it may be expensive to build, we are guessing at around 1k€. We assume that a red teamer (for who this drone is mainly intended) will have such a budget available if he is hunting big game.

---
# The hacking package
The 0x00Drone consists of two parts:
* The drone, as we have already discussed above.
* The hacking package.

The hacking package is a micro-computer (like a Raspberry Pi) that is attached to the drone and communicates with the attacker over 3G/4G data networks, thus making it completely independent from the drone. **This allows the hacking package to be ejected from the drone.** This is extremely handy to make physical backdoors because the package can survive for up to a week on it's own.

The hacking package is what contains the Linux OS and will be used for hacking. We will use a raspberry pi.

The hacking package is supposed to be ejectable from the drone and to be picked up again.

Furthermore, Leeky is the software engineer of the crew and handles the software on the micro-computer. He has made it possible to let the package communicate to the attacker over a TOR hidden service, so even when captured and if the self-destruct fails, they only have limited proof against you.

Below is a badly-drawn communication architecture of the 0x00Drone made by me. The "0x00Drone framework" is a misleading name: it is just a CLI app to communicate to the package that contains some custom scripts.
![0x00drone1|690x452](https://0x00sec.s3.amazonaws.com/optimized/2X/a/a931c08f7b748d2c688b26b10e890d7f3e55f883_1_690x452.png)

I am the hardware designer of the crew. Currently I am developing a **self-destruct mechanism** to destroy the SIM-card since that is the only thing that could lead back to you. The best approach to this is by blowing up a capacitor. The self-destruct has two modes: normal and paranoid. In normal mode, you can request a snap from the on-board RPi camera and then choose to destroy the evidence. In paranoid mode, you will be sent an alert and a snap from the camera if the camera detects any movement. If you don't respond within 30 seconds when the alarm was first triggered, it will continue to blow up anyway. This self-destruct is only useful when the hacking package has been ejected from the drone and is serving as a physical backdoor. Besides, triggering the self destruct mid-air also damages the drone, so it will probably be locked when it is attached.

---
# Firmware
ricksanchez has obtained firmware for the drone. What this might allow us to do is that the hacking package can directly interact with the drone and the other way around. There is certainly a use for this.

---
# FAQ

**When will the first prototype be released?**
> When it is done.

**When will the first prototype be done?**
> When it is released.

**Will the project be open source?**
> Of course it will be! You can find us on our Github https://github.com/Phoenix750/0x00Drone

**How does the self destruct work?**
> Electrolytic capacitors have a constant polarity. If you put a reversed polarity over them, it blows up. The more voltage you put over it and the bigger the capacity of the capacitor, the bigger the boom. Since the SIM card is the only thing that has to be blown up (the SD card of the hacking package is encrypted with LUKS), we tape the capacitor around the external antenna. In case of emergency, we put a high-voltage reverse polarity over the capacitor to blow it up.

**Isn't an exploding capacitor dangerous for injuries?**
> Yes, but it is still way less harmful than napalm or thermite, which was also an option.

**Who does what?**
> **Phoenix750** makes the customized hardware and programs the main microcontroller for said hardware.

>**Leeky** is working on the software that is present on the micro-computer and the attacker's device.

>**ricksanchez** keeps himself busy with decoding and modifying the firmware that is already flashed into the drone for our use.

**Can we aid the project?**
> Of course you can! Here's how:
> * When we feel confident in making a prototype we will open a crowdfunding campaign. You can donate.
> * Give ideas for features.
> * If you have made a modification to our software, please contact one of us and we will have a look if we can merge it.
> * Cheer us from time to time. Monkeys need motivation to do their tricks ;)

FAQ is still under construction!

---
# Features you can expect in the future:

* **Paratrooper mode:** at the moment, the only way to detach the hacking package from the drone is by landing the drone first. Uncoupling it in the air will smash the hacking package to the ground and break it. Inspired by the way that [military paratroopers jump in real life](https://youtu.be/R-2puqqmycM?t=3m11s), I intend to make a parachute system with either a static line or with height sensors, so the hacking package can be dropped in mid-flight. With height sensors it should be easier hardware-wise, with a static line it should be easier software-wise. With height sensors the stealth factor also increases because we can do a HALO-drop that way.

---
# We need your help!

We are still looking for help from within the community. I need someone who is familiar with 3D printers and is able to design 3D printed objects. We need a case around the pi to protect it from the weather and also a system to attach the coupling system to the drone.
