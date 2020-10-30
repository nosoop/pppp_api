# libPPPP_API

## About

`libPPPP_API` appears to be a custom UDP protocol library used for a number of security cameras,
including ["some random, noname spy camera from usual Chinese sources"][1], and the Uniden G755.

It appears to contain code related to the DID, which is a unique identifier for each security
camera system (that is, the central control unit that connects to the internet).

This repository is intended to chronicle the attempt to reverse-engineer the protocol well
enough to access the devices from LAN and possibly over the internet.

There's very little on this subject; the other resources I could find are
["PPPP API: what I know"][2], [its sibling article][1], and [this gist][3].

[1]: https://re-ws.pl/2018/05/security-analysis-of-spy-camera-sold-by-chinese-suppliers-iminicam-app/
[2]: https://re-ws.pl/2018/05/pppp-api-what-i-know/
[3]: https://gist.github.com/dannysperry/23fee9c11259e599fcbd

## Uniden Guardian 2

I will be using [`com.p2pcamera.app01`][unideng2] (Uniden Guardian 2) as the reference, as that
is the app that originally interoperated with the camera system that I own.  The version on hand
is 2.1.26, which still appears to be the latest available of that particular app
(considering it's been superceded by an equally shitty replacement under a new name).

Decoding the initializer string passed from the app to the library provides three IP addresses,
all of which appear to point to Amazon-related services in the United States, Asia, and Ireland
as of 2020.

[unideng2]: https://play.google.com/store/apps/details?id=com.p2pcamera.app01
