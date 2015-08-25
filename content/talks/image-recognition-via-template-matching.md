type: session
title: "Image recognition via template matching"
slug: "image-recognition-via-template-matching"
url: "talks/image-recognition-via-template-matching/index.html"
body_class_hack: talks
---

### Katie Barr

Image recognition, also known as template matching, is a key component of computer vision, and in this talk I will tell you how its done by describing algorithms used by OpenCV. The purpose of the talk is to give a practical introduction to this subject by describing both the theory and Python implementation.

Whilst the algorithms I describe are very simple, and intuitively understood, if you do not take care when implementing them you can end up with extremely inefficient computations. This is because you effectively compare every pixel in your image with every pixel in your template. These algorithms are called: correlation, correlation coefficient, and squared difference, all with or without normalisation. Normalisation is required to prevent false positives due to bright spots in images. I will explain why computing the value directly can lead to prohibitively slow computations. In order to efficiently implement the algorithms we must use a theorem called the convolution theorem, which uses Fourier Transforms. I give the Fourier Transform expressions for the template-image comparison, and this is what we use in our implementation.

I will introduce the algorithms and explain how they work, and then briefly introduce the Fourier Transform. This gives us everything we need to get started implementing our own image recognition with help from scipy and numpy. We will see how adjusting parameters in the algorithm can lead to very impressive results- the demo showing a range of letters, with different antialising, on different tiled backgrounds. By selecting how close your candidate match must be to the template at different stages during the algorithm, you can find matches with apparently large differences to the template, with no false positives. 

Whilst I will aim to ensure that the talk is comprehensible to those who haven't met Fourier Transforms before by introducing them in detail, with examples, I also hope those who have met them before will find the talk interesting, as they may not have seen this application. Whilst I apply the techniques to images, they can be used for anything which can be treated as a function.
