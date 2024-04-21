# DhyanaVR
"It is only after we learn to conduct our thoughts, speech, and action in a balanced manner and can enjoy the objects of our senses as a matter"of choice that we reclaim our joyful mind".
~ Patanjali Yogasutra  400 CE


<img width="300" alt="50" src="https://github.com/pvjambur/Dhyana_VR/assets/145439975/25a07aa0-979e-4e76-a4a7-c781ef3e98a7">


## Virtual Reality Therapy & Rehabilitation

Virtual reality therapy and rehabilitation for short term stress and fatigue conditions in athletes and office workers. Dhyana VR provides an AI based solution for reducing stress and/or fatigue in specific individuals, in the short term through the combination of VR - headsets. Dhyana VR can also be used for transforming the state of mind from alert to deep sleep and drowsiness to alert state. The stress, fatigue, alertness and sleep sate state is constantly measured using vital HRV parameters like SDNN, HF, LF and LF/HF values along with other body vital parameters, including respiration rate, blood pressure and spO2. An AI based recommendation is used to select right stimulus like music , Bi-Neural frequency, Visual scenery and personalised guided  meditation through voice using VR headset while measuring the above stated parameters and constantly making changes to the stimulus. This experience can be enabled on existing VR headsets like Apple Vision Pro. 


### Background: 


We know from the past research that transitioning the state of feeling:
a) From stress to relax
b) Fatigue to energetic
c) Wakefull-ness to deep - sleep
d) Drowsy to alertness
is possible by apply right meditation techniques.

We also know that HRV time and frequency analysis can provide  accurate state of feeling in humans   in combination of following vital health data 
i) spO2
ii) Age
iii) Gender
iv) Blood pressure

By knowing the current and desired state of feeling by the customers and measuring HRV and other health vitals continuously we then provide an immersive experience where we  superimpose  AI - recommended:
1) Visual themes
2) Relaxing music
3) Bi -neural  frequencies
4) Dynamic guided steps through voice

using a through binocular VR headset.


In contrast to traditional therapeutic approaches which often involve physical therapy and medication and  may not be sufficient for all patients. We aim to create a VR experince which can simulate a desired  environment through virtual reality, stimulating a state of minds as indicated above 


### Objective :
To develop a Virtual Reality (VR) Therapy & Rehabilitation platform built through 'Swift' (integrated with Vision Pro dynamics) that leverages the immersive and controlled environment to create a blissful space for meditation.
The user can wear the VR headset on the go; isolated VR headset "Apple Vision Pro". Further parameters such as heart rate, spO2 (blood oxygen) & pulse rate can be measured through the "Apple Watch Series 9".

<img width="300" alt="50" src="https://github.com/pvjambur/Dhyana_VR/assets/145439975/860acd27-8d2d-46bb-9c2a-64cb77c1a09d">


Traditional anti stress and anti fatigue  therapy involves deep breathing, yoga and a combination of ayurvedic and synthetic medications giving temporary relief. However, our objective is to emphasize deep breathing & yoga; integrated with music therapy for HRV, frequency therapy for & the mind & image - sound sensory combination to improve the breathing cycle. We use multiple neurobiology and cardiovascular terms to generate an overall progress report of the person.


## Installation
1. Clone this repository to your local machine using:

```bash
git clone https://github.com/pvjambur/Dhyana_VR.git
```
2. Navigate to the project directory:

```bash
cd Dhyana_VR
```
3. Install the required dependencies from `requirements.txt` using pip:
```
pip install -r requirements.txt
```
4. Clone this repository using `git clone` and deploy using the command:
```bash
streamlit run main.py
```
5. To work with the VR, if you posses a Virtual reality headset, go on and relish you meditation session, if not, we have 3D visuals for you!


## Project Highlights 

<img width="3424" alt="Untitled-6" src="https://github.com/pvjambur/Dhyana_VR/assets/145439975/52000a29-a3b2-4baa-abb2-c7a087594266">

The following flowchart gives an in-depth analysis of our project and its working procedure.

### Heart Rate, HRV & Pulse interpolation
Based on the monitored heart rate and pulse, we can interpolate the dynamic HRV of the person. Two main formulas are used to calculate HRV: RMSSD and SDNN.

#### RMSSD - the root mean square of successive differences
A standard statistical measure of HRV. It stands for the root mean square of successive differences. RMSSD HRV measures the time difference between each successive heartbeat in real-time to arrive at your RMSSD score, meaning you can see the result at the exact moment. This formula helps investigate the impact of training loads and recovery processes.

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/0293ff08-ea77-4f7c-9e1f-c7d6895e6b3b)

Researchers have proposed the following HRV RMSSD normal ranges in different studies:

19 – 48 ms — healthy adults in the age group of 38 – 42 years
35 – 107 ms — elite athletes

An important feature of RMSSD is that it characterizes short-term rapid changes in heart rate, which can only occur under the influence of the parasympathetic nervous system. It is important to assess the performance of the parasympathetic system and analyze HRV, taking into account rapidly changing metrics.

#### SDNN - the standard deviation of NN intervals
SDNN is a measure of HRV that calculates the average value of HRV in milliseconds and shows how far your HRV is from that average at any point in the day. Although it is often calculated in 24 hours.
The SDNN is considered the “gold standard” for medical stratification of cardiac risk. SDNN values predict both morbidity and mortality.

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/a1c28c89-0962-441e-ac62-7d9e8f31eeeb)

Heart attack patients with SDNN values over 100 ms have been reported to have a 5.3 lower mortality risk than those with under 50 ms.

#### pNN50 - another notable measure of HRV

Shows how active your parasympathetic system is relative to the sympathetic nervous system. The higher the value, the more relaxed the body is. If the pNN50 is low, you’re either tired or over-stressed.
This measure helps assess parasympathetic activity from 24-hour ECG recordings, and the study presented supporting data by comparing pNN50 values in healthy subjects with those with diabetes mellitus and patients who’ve had a heart transplant.

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/5e29b85b-6684-45d2-929c-e007c4d053df)


### Audio and HRV interpolation

These factors are the major connectors between HRV monitoring and music therapy. Let us go in deep and understand the factors which interpolate and graph parameters from audio and HRV inputs.

#### HRV Frequency Measurements (LF, HF, LF/HF)

 Common Frequency Domain HRV metrics include:

  High-Frequency power (HF): frequency activity in the 0.15 - 0.40Hz range (green in the above chart)
  Low-Frequency power (LF): frequency activity in the 0.04 - 0.15Hz range (yellow in the above chart)
  LF/HF Ratio: A ratio of Low Frequency to High Frequency. Some consider this indicative of Sympathetic to Parasympathetic Autonomic Balance, but that is controversial.

Time-Domain Parameter:

  RR: interval between two heartbeats (R spikes in the QRS complex / ECG).
  NN: interval between two heartbeats (emphasis on "normal" heartbeats)

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/ce0e5eca-0c9b-4f77-a398-71eb55420601)


The pure RR intervals can be decomposed into their frequency constituents using a fast Fourier transformation (FFT). By this method, frequency components in the VLF, LF and HF spectra are obtained from the signal. The total power is indicated as TP.

It has been shown that the frequency-based HRV parameters (spectral analysis) are not the ideal solution for the use in practice as they are very accident-sensitive. For instance the VLF (very low frequency) area can simply not be represented correctly in a short-term measurement.
 
Therefore, the ANS Analysis is limited to the time-domain parameters as they are valid for the short-term measurement.

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/2362ab41-86a3-4e7b-9edd-c43114d8eb51)

Reading duration should be a minimum of 5 minutes to be accurate. 2 minutes is for confidence in Low Frequency (LF) values. High frequency (HF) can reliably be measured in 60 seconds. You can start to measure LF in as little as 2 minutes, but research says 2 minutes+ is best for LF.

In theory, LF/HF shows ANS balance 

Low LF/HF ratio = PSNS dominance 

High LF/HF ratio = SNS dominance

Source: EHRV & ansAnalysis


#### Music & Sound Therapy

Music treatment, also known as music therapy, or so called music medicine, is a newly developed interdisciplinary
treatment including music, medicine and psychology.

Heart rate variability (HRV), as the name suggests is the variation in the heart rate of an individual. More precisely, HRV is the minute fluctuations in the time interval (typically tens of milliseconds long) between successive heartbeats or in an electrocardiogram (EKG), two adjacent Q-Q (or N-N) intervals. 

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/c8a60d71-181d-4591-9818-c915526ac42e)

Before Music

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/e27b0a53-344e-436f-81eb-65d5c140699d)

During Music

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/1d34e134-9f87-4808-849b-088a45bc03a9)

After Music

Source:  Tianjin University, Tianjin (2010)

The LF component is considered to reflect the activity of the whole autonomic nervous system. In our study, the LF component generally increased, indicating that this type of music increased the activity of the whole autonomic nervous
system.

The LF / HF ratio is a reflection of the coordination of the sympathetic nervous system and parasympathetic nervous system. The overall variation was not obvious.

The ApEn is an indicator of system’s complexity. In our study, ApEn decreased after music therapy, which indicates that the system becomes less complexity, with less frequency components.

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/3cf2da14-14f6-43f7-9046-69a6ffb43317)

The following shows the pre and post music therapy conducted GIMS (India)

There are ancient texts and modern studies alluding to the therapeutic benefits obtained from listening to music. Studies have shown that chanting "OM" has a relaxing effect by causing parasympathetic dominance, limbic deactivation, and decreasing the brain's dopamine levels. This research aims to study the effect of listening to OM chanting on the cardiovascular system and heart rate variability and its possible use as a stress buster among medical students.


## Setup 

### Hardware Setup

Our project is monitored by two devices: Apple Vision Pro and the Apple Watch series, with an additional nose-mist add-on.

A 'Swift' based app which can be integrated with Vision Pro.

![image](https://github.com/pvjambur/Dhyana_VR/assets/145439975/62b1618e-c0d3-4292-a311-aef4b982fadd)

Consists of VR display showing the immersive environment interaction, with a dashboard consisting of vitals, records and other factors. The Apple watch provides multiple parameters such as; blood oxygen levels (spO2), pulse, heart rate (bpm) and blood pressure. The following would be displayed in the dashboard as well.

<img width="400" alt="50" src="https://github.com/pvjambur/Dhyana_VR/assets/145439975/5f9a197e-15d0-4533-93b0-9418d8ab0484">

### Software design

The dashboard gives a clear view of the dynamic status of the user. At the end of the therapy, it generates an Excel file giving a detailed report of the therapy session and the improvements made by the user. 

<img width="400" alt="50" src="https://github.com/pvjambur/Dhyana_VR/assets/145439975/87558fe3-2567-4d9f-ae53-c5412e72ea37">

Sample dashboard display, user perspective.

It gives the details of the user's progress and additional information achieved by the user.

## Architechture & Future Scope

<img width="3424" alt="Untitled-6" src="https://github.com/pvjambur/Dhyana_VR/assets/145439975/52000a29-a3b2-4baa-abb2-c7a087594266">

The following flowchart gives an in-depth analysis of our project and its working procedure.

### Steps of our project

#### Hardware deployment

The user will be wearing the Apple Vision Pro and Apple series watch, and have a Bluetooth-paired iPhone connected to the watch.

#### Theme and audio analyser

Based on the various HRV, HF, lF & LF/HF ratios recorded by the watch, the system suggests the appropriate theme and audio frequency to be displayed to the user for the most optimum results.

#### Meditation process

The AI guides the entire meditation procedure while displaying the dashboard on the VR screen. Users may change the theme or audio appropriately. Based on various waves and their functions as mentioned in the flowchart, the AI gives the best outcome by varying the pitch of the music according to the 'Principles of Music therapy'.

#### Nostril passage

Cold air can stimulate deep breathing and can improve the breathing cycle. A separate device will be given to the user which can be placed on the nose which spreads cold air near the user's nose, to bring about freshness prompting them to breathe deeply. Cold air has been used for a long for the same procedure, the reason why Yogis meditate in the mountains.


#### Aroma infusion and therapy

Aroma infusion with the given nostril air add-on can lower stress levels in users quite rapidly. Multiple volatile yet safe non-polar liquids are infused in as mist-like - like - form which causes no harm to users, yet ensures that the user inhales less amount over a long period.

Aromatherapy stimulates the presence of the user near lakes, meadows etc, given a $D - an immersive experience, encapsulating every sensory response of the user.

#### Overall Immersive Experience

Based on the following parameters, the users get the best experience during the entire phase of meditation. Once the session is over, it gives a detailed report of the user's progress throughout the
session.


## Homepage 
<img width="900" alt="50" src="https://github.com/pvjambur/Dhyana_VR/blob/main/home.png">

## Results

Watch the [Our Project Demonstration Video](https://youtu.be/FoMxzM03sQU)

## More Information about the Project
Refer to [Our project Pitch](https://www.canva.com/design/DAGC4YS7vm8/ekBtb1hNoaM3r-oZldobXQ/edit?utm_content=DAGC4YS7vm8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## About us

The collaborators of this GitHub repository are Pranav V Jambur and Smruthi S Kadagadkai, pursuing bachelors in Engineering, batch of 2027.

## Bibliography

[link1](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2017.00360/full)
[link2](https://www.theguardian.com/books/2017/may/07/ice-baths-and-snow-meditation-can-cold-therapy-make-you-stronger-what-doesnt-kill-us-scott-carney)
[link3](https://pubmed.ncbi.nlm.nih.gov/29424499/)
[link4](https://www.ans-analysis.com/hrv/hrv-measuring-parameter.html)
[link4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10008213/#:~:text=Thus%2C%20following%20the%20same%20lines,should%20have%20a%20relaxing%20effect.)
[link5](https://www.gqmiddleeast.com/news/apple-reveals-new-vr-headset-vision-pro)
[link7](http://asr.cs.cmu.edu/spring2012/lectures/music.therapy.on.heartrate.variability.pdf)
[link8](https://www.cureus.com/articles/135577-short-term-effect-of-spiritual-music-on-heart-rate-variability-in-medical-students-a-single-group-experimental-study#!/)


