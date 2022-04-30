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
**Mean-shift** will make clusters from a centriod and iterate this until it hit the area with the most density within a specific radius. This radius is known as a bandwitdh and slides around the datapoints as a kernel. The centerpoint of the radius is determined by the mean of the points within the kernel. An advanteges with Mean-shift is that it only needs the parameter called bandwidth(radius), which will determin the optimal number of clusters. Furthermore there is no issue with minimun distance which can cause chain clustering with K-means. A disadvantage with Mean-shift can be that it does not work well with high a number of dimensions. Also the radius has to be pre-defined and is slower when compared to K-means.  
**K-means** will make the number of clusters as specified by K. Each data point is closer to it's own cluster center. The clusters will be made iterative since the algorithm iterates through the datapoints. The optimal number of K can be measure by two methods, either the elbow method which is calculated out from the lowest distorion (error) or the Silhouette method which estimates how close points are to other points in the cluster and how far it is from other clusters. Advantages with K-means can be that it is fairly simple, effective (always gives a solution even though it isn't always a good answer) and it is quick. Disadvantages could be that it only uses numeric data, sensitive to outliers, difficult to estimate the quality and only good for compact clusters.
  
• in which occasions would you prefer to use the mean shift algorithm?  
I would prefer to use Mean-shift when having to classify my datapoint without having prior knowledge about the number of clusters and I know I am working with a dataset with high density regions. 
