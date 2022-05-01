# Assignment 9: Clustering

## Group Members

- Allan Bo Simonsen, cph-as484
- Jean-Poul Leth-Møller, cph-jl360
- Nina Lisakowski, cph-nl163


#### The objective:
Practicing unsupervised machine learning: clustering.  
The tasks:  
1. In Exercise 1 we used Hierarchical clustering algorithm.  
    - Which type?  
      Hierarchical clustering is an unsupervised learning algorithm that groups similar objects into groups called clusters.  
      We used the agglomerative hierarchical clustering algorithm in exercise 1.  
  
  
    - How many types of hierarchical clustering are you familiar with?  
      We know of two types of hierarchical clustering.  
      These are:  
          - Agglomerative  
          - Divisive  
    
    - How do they differ?  
        - Agglomerative clustering:  
        In agglomerative clustering each data point is treated as a seperate cluster. The algorithm calculates the two clusters that have the shortest distance between them and then combines them into one cluster. It repeats this action until all the data points are combined into one single cluster. The distance between clusters are calculated using either the Manhatten or euclidean distance. You can then choose the optimal amount of clusters based on a dendrogram where you place a horizontal line, where this has the largest distance to the adjacent horizontal lines. There are a few ways to combine clusters when calculating distance between them.
          - Single linkage: Two closests points in each cluster.  
          - Complete linkage: Two furthest points in each cluster.  
          - Average linkage: Distance between centroids of the two clusters.  
    
        - Divisive clustering:  
        In Divisive clustering we do the opposite of agglomerative clustering. Meaning, we start by having one big cluster with all data points in it. You then begin to divide the cluster into two smaller clusters, this is based on what data points are the most dissimilar. This is repeated until each data point is in its own cluster.  
      Therefore divisive is the top-down approach and agglomerative is the bottom-up approach.  
  
2. Train a clustering model with Mean Shift algorithm and freedom.csv data source file.  
    - Store your model in a file.
       - The solution to this task can be found in the jupyter notebook.   
    - Create simple web application that can deploy and run the model as seen in class.  
      - The solution to this task can be found in the jupyter notebook.  
    - Run the application for predicting the cluster of a data set.
      - The solution to this task can be done and found in the jupyter notebook.  
    - Note about PCA.  
      - We used PCA to reduce the dimension of the dataset. This is because the mean shift algorithm could only produce one cluster with all 47 columns as input. Therefore we decided to use PCA to reduce down to two features. This produced five clusters when running the mean shift algorithm.
    - Take and attach a screen shot of your solution.  
    ![Billede](https://github.com/Jean-Poul/Assignment-9-Clustering/blob/main/Udklip1.PNG)  
    ![Billede](https://github.com/Jean-Poul/Assignment-9-Clustering/blob/main/Udklip2.PNG)  
    
    On the picture below the result from the above input can be seen and the result is that it belongs to cluster 2.
    ![Billede](https://github.com/Jean-Poul/Assignment-9-Clustering/blob/main/Udklip3.PNG)  
  
3. Describe the difference between K-means and Mean Shift algorithms.  
    - K-means and Mean-shift are both used in unsupervised learning which are used for clustering. The difference between them is that with K-means you will have to specify the number of clusters while the Mean-shift algorithm will determine this by itself.  
**Mean-shift** will make clusters from a centriod and iterate this until it hits the area with the most density within a specific radius. This radius is known as a bandwitdh and slides around the data points as a kernel. The centerpoint of the radius is determined by the mean of the points within the kernel. An advanteges with Mean-shift is that it only needs the parameter called bandwidth(radius), which will determine the optimal number of clusters. Furthermore, there is no issue with minimun distance which can cause chain clustering with K-means. A disadvantage with Mean-shift can be that it does not work well with a large number of dimensions. Also the radius has to be pre-defined and is slower when compared to K-means.  
**K-means** will make the number of clusters as specified by K. Each data point is closer to it's own cluster center. The clusters will be made iterative since the algorithm iterates through the data points. Two of the methods that can be used to determine K is the Elbow method which is calculated from the lowest distortion, mean squared error, and the Silhouette method which estimates how close points are to other points in the cluster and how far it is from other clusters. Advantages with K-means can be that it is fairly simple, effective, always gives a solution even though it isn't always a good answer, and it is quick. Disadvantages could be that it only uses numeric data, sensitive to outliers, difficult to estimate the quality, and only good for compact clusters.
  
  - In which occasions would you prefer to use the mean shift algorithm?  
    - We would prefer to use Mean-shift when having to classify our data without having prior knowledge about the number of clusters and when we know that we are working with a dataset with high density regions. Mean shift can have a poor performance when working with a large number of dimensions which results in it returning one cluster. Mean shift works well when working with image processing, as it is good to detect patterns as it can group the colours together.
