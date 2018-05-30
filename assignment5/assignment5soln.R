setwd('/Users/paul/Dropbox/DataScience/datasci_course_materials/assignment5')
library(caret)
library(rpart)
library(randomForest)
library(e1071)

df <- read.csv('seaflow_21min.csv')
summary(df)
head(df)

train_ids <- createDataPartition(df$pop, p = 0.8, list = F)
df_train <- df[train_ids, ]
df_test <- df[-train_ids, ]
mean(df_train$time)

ggplot(df, aes(pe, chl_small)) + geom_point(aes(color = pop))

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=df_train)
print(model)
predictions <- predict(model, df_test, type = 'class')
sum(df_test$pop == predictions) / nrow(df_test)
table(pred = predictions, true = df_test$pop)

model <- randomForest(fol, data=df_train)
predictions <- predict(model, df_test, type = 'class')
sum(df_test$pop == predictions) / nrow(df_test)
importance(model)
table(pred = predictions, true = df_test$pop)

model <- svm(fol, data=df_train)
predictions <- predict(model, df_test, type = 'class')
sum(df_test$pop == predictions) / nrow(df_test)
table(pred = predictions, true = df_test$pop)

vars <- c(fsc_small, fsc_perp, fsc_big, pe, chl_small, chl_big)
ggplot(df, aes(x = fsc_small)) + geom_histogram()
ggplot(df, aes(x = fsc_perp)) + geom_histogram()
ggplot(df, aes(x = fsc_big)) + geom_histogram()
ggplot(df, aes(x = pe)) + geom_histogram()
ggplot(df, aes(x = chl_small)) + geom_histogram()
ggplot(df, aes(x = chl_big)) + geom_histogram()

ggplot(df, aes(time, chl_big)) + geom_point(aes(color = pop))

library(dplyr)
df_new <- filter(df, file_id != 208)
train_ids <- createDataPartition(df_new$pop, p = 0.8, list = F)
df_train <- df_new[train_ids, ]
df_test <- df_new[-train_ids, ]

fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, method="class", data=df_train)
print(model)
predictions <- predict(model, df_test, type = 'class')
sum(df_test$pop == predictions) / nrow(df_test)
table(pred = predictions, true = df_test$pop)

model <- randomForest(fol, data=df_train)
predictions <- predict(model, df_test, type = 'class')
sum(df_test$pop == predictions) / nrow(df_test)
importance(model)
table(pred = predictions, true = df_test$pop)

model <- svm(fol, data=df_train)
predictions <- predict(model, df_test, type = 'class')
sum(df_test$pop == predictions) / nrow(df_test)
table(pred = predictions, true = df_test$pop)