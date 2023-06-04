**Leukemia Detection Using Image Processing Techniques**

Microscopic imaging is the process of capturing and visualizing images of objects or samples that are too small to be seen by the naked eye. This is achieved through the use of a microscope and various imaging techniques, including brightfield, darkfield, phase contrast, and fluorescence microscopy. Microscopic imaging is widely used in various fields, such as biology, medicine, material science, and nanotechnology, for the study of cell structure, tissue analysis, and the examination of small samples.

A blood smear, also known as a peripheral blood smear or a blood film, is a laboratory test used to evaluate the components of a person's blood, including red and white blood cells and platelets. The test is often performed to diagnose conditions such as anemia, infections, bleeding disorders, and other blood disorders.

Image processing is required in blood smear tests as it helps in the automatic and objective analysis of blood cells. In a blood smear test, a thin layer of blood is spread on a glass slide and stained to visualize the different types of blood cells. Various image processing techniques are used for analysis to provide more precise and consistent results compared to manual analysis. Some of the image processing techniques used are

- Image enhancement: Microscopic images are low contrast images which make diagnosis difficult.Image enhancement techniques can be used to improve the quality and clarity of microscopic images. These techniques include filtering, sharpening, and contrast enhancement.
- Image Segmentation: It is used to separate the different components of the blood smear, such as red blood cells, white blood cells, and platelets, from the background.



**Implementation of the image segmented technique:**

- Thresholding is applied to enhanced images.
- Erosion with a suitable mask is applied to the image.
- Dilation with the same mask is applied to the eroded image to obtain the opened image.
- Applying median filter to opened image to remove salt and pepper noise
- Using sobel edge detection to detect edges on the filtered opened image
- The edges detected are leukemia cells

**Implementation of the image segmented technique:**

- Thresholding is applied to enhanced images.
- Erosion with a suitable mask is applied to the image.
- Dilation with the same mask is applied to the eroded image to obtain the opened image.
- Applying median filter to opened image to remove salt and pepper noise
- Using sobel edge detection to detect edges on the filtered opened image
- The edges detected are leukemia cells

**Input Image** 

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.001.png)

**GreyScale Image:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.002.png)

**Contrast stretched image:** 

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.003.png)

**Median Filtered contrast stretched image:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.004.png)

**Histogram Equalized Image:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.005.png)

**Median Histogram Equalized Image:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.006.png)

**Enhanced Image:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.007.png)

**Image after Thresholding:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.008.png)

**Image after opening:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.009.png)


**Opened Image after applying median Filter:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.010.png)

**Edge Detected image:**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.011.png)


**Original image 						Segmented Image**

![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.012.png) 		**![](Aspose.Words.b373b9b1-447e-4c6b-a0d3-4eb857332b80.013.png)**

**References:**

1) Gitanjali Ganpatrao Nikam, Shuchi Singh, Priya Singh, Radhika Sarraf: “A Comprehensive Study of Medical Image Analysis”, IEEE (2019). 

<https://ieeexplore.ieee.org/document/907999>

1) Al-jaboriy, S. S., Sjarif, N. N. A., Chuprat, S., & Abduallah, W. M. (2019). Acute lymphoblastic leukemia segmentation using local pixel information. Pattern Recognition Letters, 125, 85-90.

<https://www.sciencedirect.com/science/article/abs/pii/S0167865519301072>

1) Raje, C., & Rangole, J. (2014, April). Detection of Leukemia in microscopic images using image processing. In 2014 International conference on communication and signal processing (pp. 255-259). IEEE.

`	`<https://ieeexplore.ieee.org/abstract/document/6949840>

Nitish J S - https://github.com/Nitish-JS
