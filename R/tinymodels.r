library(tidymodels)

# intial_split() built to seperate data set  into training and testing sets--default 3/4 training
# prop argument can change the default

iris_split <- initial_split(iris, prop = .6)
iris_split