# Deploy Optimal Model Using Plumber Package

library(plumber)
library(glmnet)
library(methods)
model <- readRDS(file='../data/optimal_model.elasticnet.rds')

#' @param Age age
#' @param G games
#' @param GS games started
#' @param MP minutes played
#' @param PER player efficiency ranking
#' @param TS. true shooting percentage
#' @param X3PAr 3 point attempts over field goal attempts
#' @param FTr free throw rate
#' @param ORB. offensive rebound perecentage
#' @param DRB. defensive rebound percentage
#' @param TRB. total rebound percentage
#' @param AST. assist to turnover percentage
#' @param STL. steal percentage
#' @param BLK. block percentage
#' @param TOV. turnover percentage
#' @param USG. usage percentage
#' @param OWS offensive wins shares
#' @param DWS defensive wins share
#' @param WS win shares
#' @param WS.48 win shares over 48
#' @param OBPM offensive box plus minutes
#' @param DBPM defensive box plus minutes
#' @param BPM box plus minutes
#' @param VORP value over replacement player
#' @param FG field goals
#' @param FGA field goal attempts
#' @param FG. field goal percentage
#' @param X3P 3 pointers
#' @param X3PA 3 point attempts
#' @param X3P. 3 point percentage
#' @param X2P 2 pointers
#' @param X2PA 2 point attempts
#' @param X2P. 2 point percentage
#' @param eFG. effective field goal percentage
#' @param FT free throws
#' @param FTA free throw attempts
#' @param FT. free throw percentage
#' @param ORB offensive rebounds
#' @param DRB defensive rebounds
#' @param TRB total rebounds
#' @param AST assists
#' @param STL steals
#' @param BLK blocks
#' @param TOV turnovers
#' @param PF personal fouls
#' @param PTS points
#' @post /predict_salary
function(Age=0, G=0, GS=0, MP=0, PER=0, TS.=0, X3PAr=0, FTr=0, ORB.=0, DRB.=0, TRB.=0,
         AST.=0, STL.=0, BLK.=0, TOV.=0, USG.=0, OWS=0, DWS=0, WS=0, WS.48=0, OBPM=0, 
         DBPM=0, BPM=0, VORP=0, FG=0, FGA=0, FG.=0, X3P=0, X3PA=0, X3P.=0, X2P=0, 
         X2PA=0, X2P.=0, eFG.=0, FT=0, FTA=0, FT.=0, ORB=0, DRB=0, TRB=0, AST=0, STL=0,
         BLK=0, TOV=0, PF=0, PTS=0){
  vec <- c(Age,G,GS,MP,PER,TS.,X3PAr,FTr,ORB.,DRB.,TRB.,AST.,STL.,BLK.,TOV.,USG.,
             OWS,DWS,WS,WS.48,OBPM,DBPM,BPM,VORP,FG,FGA,FG,X3P,X3PA,X3P.,X2P,X2PA,
             X2P.,eFG.,FT,FTA,FT.,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS)
  mat <- matrix(as.double(vec),1,46)
  mat <- data.matrix(mat)
  vals <- predict(model,s=model$lambda.min,newx=mat)
  return(vals)}
