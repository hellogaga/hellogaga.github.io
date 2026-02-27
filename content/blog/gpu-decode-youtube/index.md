---
title: "Trying Using GPU to decode video when watching Youtube"
date: 2021-03-11
summary: "Attempting to enable GPU hardware video decoding for YouTube playback on Ubuntu with an Nvidia GTX 1050."
categories:
  - Blog
tags:
  - linux
  - Ubuntu
  - Nvidia
  - GPU
---

## High CPU use when watching youtube.

Configuration of PC

- Ubuntu 20.04
- i5-6600K
- 4\*8Gb
- GTX 1050 (2G)

When watching a [4K@60fps video](https://www.youtube.com/watch?v=xqDuf48WyzI). The CPU usage can be around 80% and GPU usage is roughly 15%. At this time, Youtube uses vp9 as the codec. <br>
<img src="/images/youtube_cpu.png" alt="cpu usage"/>
<br>
<img src="/images/youtube_codec.png" alt="youtube codec"/>

## Solutions

I have found two tutorials online. One is for [Chrome as well as others](https://www.linuxuprising.com/2021/01/how-to-enable-hardware-accelerated.html). Another is for[Chromium](https://www.linuxuprising.com/2018/08/how-to-enable-hardware-accelerated.html). I am following the tutorial from the first one.

I enabled the following in Chrome:

```
chrome://flags/#ignore-gpu-blocklist
chrome://flags/#enable-accelerated-video-decode
```

I have installed the following packages. This step is to install the VA-API to be able to decode media.

```bash
sudo apt install i965-va-driver-shaders libva-drm2 libva-x11-2
sudo dpkg -i libvdpau1_1.4-2_ubuntu20.04.1_amd64.deb
sddo dpkg -i vdpau-va-driver_0.7.4-7ubuntu1_ppa2_20.04.1_amd64.deb
```

The NVIDIA Driver Version is 460.39. Launch the browser using `--use-gl=desktop` to enable VA-API hardware acceleration.

```bash
google-chrome-stable --use-gl=desktop
```

## Problem

After the previous steps. When playing the same video, I still have problems with high CPU usage. And the `chrome://media-internals` still shows that I am using `FFmpegVideoDecoder`. It should be `MojoVideoDecoder` which enables the GPU decoding. <br>

### Test using the extension h264ify

The extension [h264ify](https://chrome.google.com/webstore/detail/h264ify/aleakchihdccplidncghkekgioiakgal) forces the youtube video to be played with h.264 videos. This solution **worked**, but the problem is that the **4k resolution is no long available**. I can only play it with HD.

### No h264ify extension and open chrome with `--use-gl=desktop`

I uninstalled the h264ify extension and run chrome with `--use-gl=desktop`. Youtube videos cannot be played at all. <br>
<img src="/images/youtube_error.png" alt="youtube play error"/>
<br>
<img src="/images/youtube_error_code.png" alt="youtube play error"/>

## Discussion on this topic.

The following links are for archive. I do not have a solution yet. The following links might be useful:

- Nvidia Discussion [forum](https://forums.developer.nvidia.com/t/turing-vp9-decode-acceleration-not-working-on-linux/72221). An answer is:
  > Vdpau doesn't decode VP9, therefore vaapi over vdpau also doesn't decode VP9. You have never seen hardware-accelerated VP9 playback with chromium-vaapi and your old 1050Ti.
- An experimental Vdpau driver that supports vp9. [Link](https://github.com/xtknight/vdpau-va-driver-vp9)
- Nvidia GPU support [list](https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new). My GPU is GTX1050 (GP107)
- Chromium beta [PPA](https://launchpad.net/~saiarcot895).
