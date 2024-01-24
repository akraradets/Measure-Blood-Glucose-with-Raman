<h2>Table of Content</h2>

- [Measure Blood Glucose with Raman Spectroscopy](#measure-blood-glucose-with-raman-spectroscopy)
  - [Resources](#resources)
  - [What are we doing?](#what-are-we-doing)
  - [How?](#how)
  - [The rabbit hole](#the-rabbit-hole)

# Measure Blood Glucose with Raman Spectroscopy

This repository is for the ongoing research of `Measuring Glucose in Blood with Raman Spectroscopy`.

## Resources

- [To see the current status of the project](https://github.com/users/akraradets/projects/1)
- [To see to-do list (issues)](https://github.com/akraradets/Measure-Blood-Glucose-with-Raman/issues)
- [To discuss](https://github.com/akraradets/Measure-Blood-Glucose-with-Raman/discussions)
- [To read document](https://github.com/akraradets/Measure-Blood-Glucose-with-Raman/wiki)

## What are we doing?

To gold standard way to measure the concentration of glucose in blood is by sampling the blood directly (invasive).
This creates a couple of problems; (1) it hurts, (2) no continuous measurement, and (3) risk of infection.
All researchers are asking "*Can we do this in a non-invasive manner?*"

## How?

Well, based on our literature review, there are quite a handful of ways.
We could use some other samples like saliva and tears.
Or we could try to get the blood without taking the blood.

What????

Yes, it seems possible to measure the blood through the skin (transcutaneous) via a family of spectroscopy techniques.
Both **Near-Infrared Spectroscopy** (NIRS) and **Raman Spectroscopy** are being compared frequently since they are known to complement each other (absorption vs scattering).
The decisive factor is the ability to measure an aqueous sample (containing water).
This is because the water ($H_2O$) absorbs a large band of the NIR spectrum, so it is difficult to measure the substance existing in the water.
Thus, we chose to use Raman.

This decision is backed up by many publications.
Raman can be used to measure the concentration in (1) water, and (2) blood.
In addition, multiple researches show that a measurement of Raman on (3) skin can also be used to find Glucose concentration in blood.
The results show a very high correlation between the gold-standard invasive method and the on-skin Raman method, thus, luring us to this rabbit hole.

## The rabbit hole

If this is easy then we would not discuss this.
Our research group consists of one Ph.D. in Computer Science and a master's student in Data Science (who has experience in Raman measurement).
The project kicked off in 2022 but we have not been able to reproduce any publication.
