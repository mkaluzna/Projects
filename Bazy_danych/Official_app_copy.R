library(shiny)
library(RPostgreSQL)
library(DT)
library(ggplot2)
library(dplyr)

drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "seriale",
                 host = "localhost", port = 5432,
                 user = "czoppson", password = 'x')

tab1 <-  dbGetQuery(con, "SELECT * from ser_kat;")
                  
#######tabela2#######
tab2 <- dbGetQuery(con, "SELECT pr.nazwa_producenta,s.tytuł,ts.nazwisko FROM seriale as s
                   JOIN tworcy_serialu as ts USING(id_serialu)
                   JOIN produkcja as p on p.nazwa_serialu = s.tytuł
                   JOIN producenci as pr on p.id_producenta = pr.id_producenta;")
colnames(tab2)<- c('Producent','Tytuł','Nazwisko_reżysera')
######tabela3############
tab3<- dbGetQuery(con, "SELECT s.tytuł,a.imie,a.nazwisko,a.plec FROM seriale as s 
                  JOIN aktorzy as a on a.tytul = s.tytuł")

###########tabela 4 ########
tab4 <-dbGetQuery(con," SELECT s.tytuł,pr.nazwa_producenta,o.imdb,o.filmweb,o.studenci,o.srednia FROM Seriale as s 
                  JOin oceny2  as o USING(id_serialu)
                  JOin produkcja as p on p.nazwa_serialu = s.tytuł
                  JOIN producenci as pr on pr.id_producenta = p.id_producenta;")

tab5 <- dbGetQuery(con, "SELECT * from klienci;")
tab6 <- dbGetQuery(con, "SELECT * from wypozyczone;")


############# Aplikacja ################
ui<- fluidPage(
  tabsetPanel(
    ########PIERWSZY PANEL#####
    tabPanel('Informacje o dostepnosci i serialach',
             sidebarLayout(
               sidebarPanel(
                 selectInput(inputId = 'From',
                             label = 'Wybierz serial które cie intersuje by sprawdzić dostępność',
                             choices = c("Gra o Tron","Kompania braci","Narcos","Dom z papieru","Przyjaciele","Stranger Things","Maniac","Seks w wielkim miescie"),
                             selected = 'Seriale')
                 
               ),
               mainPanel(
                 dataTableOutput(outputId = 'first_table')
               )
             )
    ),
    ######### DRUGI PANEL######
    tabPanel('Producenci i aktorzy ',
             sidebarLayout(
               sidebarPanel(
                 selectInput(inputId = 'From2',
                             label = 'Wybierz nazwę producenta',
                             choices = c("HBO","Netflix","Warner Bros"),
                             selected = 'Netflix'),
                 selectInput(inputId = 'From3',
                             label = 'Z jakiego serialu intersują cie aktorzy',
                             choices = c("Gra o Tron","Kompania braci","Narcos","Dom z papieru","Przyjaciele","Stranger Things","Maniac","Seks w wielkim miescie"),
                             selected = 'Dom z papieru')
               ),
               mainPanel(
                 dataTableOutput(outputId = 'producenci'),
                 dataTableOutput(outputId = 'aktorzy')
               )
             )
             
    ),
    tabPanel('Oceny',
             sidebarLayout(
               sidebarPanel(
                 selectInput(inputId = 'x',
                             label = 'Oś_X',
                             choices = c('imdb','filmweb', 'studenci'),
                             selected = 'imdb' ),
                 selectInput(inputId = 'y',
                             label = 'Oś_Y',
                             choices = c('imdb','filmweb','studenci'),
                             selected = 'filmweb')
                 
               ),
               mainPanel(
                 dataTableOutput(outputId = 'oceny'),
                 plotOutput(outputId = 'scatterplot')
                 
               )
               
             )
    ),
    tabPanel('Wypożyczenia i klienci',
             sidebarLayout(
               sidebarPanel(),
               mainPanel(
                 dataTableOutput(outputId = 'klubowicze'),
                 dataTableOutput(outputId = 'wypo')
                )
               )
             )
    
    
  )
)

server <- function(input,output){
  output$first_table <- DT::renderDataTable({tab1%>%
      select(tytuł,rodzaj,rok,kraj,cena,dostepnosc,id_kopii)%>%
      filter(tytuł == input$From)
  })
  output$producenci <-  DT::renderDataTable({tab2 %>%
      filter(Producent == input$From2)})
  output$aktorzy <-  DT::renderDataTable({tab3 %>%
      filter(tytuł == input$From3)})
  output$oceny <- DT::renderDataTable({tab4 %>% 
      select(tytuł,imdb,filmweb,studenci,srednia)})
  output$scatterplot <- renderPlot({ggplot(tab4,aes_string(x = input$x, y = input$y, col = 'tytuł' ))+
      geom_point()})
  output$klubowicze <- DT::renderDataTable({tab5 %>%
                                            arrange(id_klienta)})
  output$wypo <- DT::renderDataTable({tab6 %>%
                            arrange(id_klienta)})
}
shinyApp(ui = ui, server = server)
