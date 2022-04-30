# Assignment 9: Clustering

## Group Members

- Allan Bo Simonsen, cph-as484
- Jean-Poul Leth-Møller, cph-jl360
- Nina Lisakowski, cph-nl163


#### The objective:
Practicing unsupervised machine learning: clustering.  
The tasks:  
1. In Exercise 1 we used Hierarchical clustering algorithm.  
• Which type?  
• How many types of hierarchical clustering are you familiar with?  
• How do they differ?  
2. Train a clustering model with Mean Shift algorithm and freedom.csv data source
file.  
• store your model in a file  
• create simple web application that can deploy and run the model as seen in class  
• run the application for predicting the cluster of a data set  
• take and attach a screen shot of your solution  
![Billede](https://github.com/Jean-Poul/Assignment-9-Clustering/blob/main/Udklip1.PNG)
3. Describe the difference between K-means and Mean Shift algorithms  
K-means and Mean-shift are both used in unsupervised learning which are used for clustering. The difference between them is that with K-means you will have to specify the number of clusters while the Mean-shift algorithm will determin this by itself.  
**Mean-shift** will make clusters from a centriod and iterate this until it hit the area with the most density within a specific radius. This radius is known as a bandwitdh and slides around the datapoint as a kernel. The centerpoint of the radius is determined by the mean of the points within the kernel. An advanteges with K-shift is that it only needs the parameter called bandwidth(radius), which will determin the optimal number of clusters. Furthermore there is no issue with minimun distance which can cause chain clustering with K-means. A disadvantage with Mean-shift can be that it does not work well with high a number of dimensions.
  
• in which occasions would you prefer to use the mean shift algorithm?  
center point is the mean of the points within the sliding
windo
