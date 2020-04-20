# Deploy Optimal Model Using Plumber Package

library(plumber)
model <- readRDS('../data/optimal_model/slr/model.rds')
year_levels <- readRDS('../data/optimal_model/slr/year_levels.rds')
Pos_levels <- readRDS('../data/optimal_model/slr/Pos_levels.rds')
Tm_levels <- readRDS('../data/optimal_model/slr/Tm_levels.rds')
#' @param year '2016' or '2017'
#' @param Pos 'C','PF','PG','SF','SG'
#' @param Age age
#' @param Tm team abbreviation or 'TOT' for traded player
#' @param G games
#' @param MP minutes played
#' @param X3PAr 3 point attempts over field goal attempts
#' @param TOV. turnover percentage
#' @param DWS defensive wins share
#' @param DBPM defensive box plus minutes
#' @param BPM box plus minutes
#' @param FG. field goals
#' @param STL steals
#' @param PF personal fouls
#' @param ovr NBA 2K Overall
#' @post /predict_salary
function(year='2016', Pos='PF',Age=0,Tm='TOT',G=0,MP=0,X3PAr=0,TOV.=0,DWS=0,DBPM=0,BPM=0,FG.=0,STL=0,PF=0,ovr=0){
  input_l <- list(
    year = factor(year,levels=year_levels),
    Pos = factor(Pos,levels=Pos_levels),
    Age = as.numeric(Age),
    Tm = factor(Tm,levels=Tm_levels),
    G = as.numeric(G),
    MP = as.numeric(MP),
    X3PAr = as.numeric(X3PAr),
    TOV. = as.numeric(TOV.),
    DWS = as.numeric(DWS),
    DBPM = as.numeric(DBPM),
    BPM = as.numeric(BPM),
    FG. = as.numeric(FG.),
    STL = as.numeric(STL),
    PF = as.numeric(PF),
    ovr = as.numeric(ovr))
  df <- as.data.frame(input_l)
  val <- predict(model,df)
  return(val)}
