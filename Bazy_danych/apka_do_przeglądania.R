library(shiny)
library(RPostgreSQL)
library(DT)

drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "seriale",
                 host = "localhost", port = 5432,
                 user = "czoppson", password = 'x')



ui <- fluidPage (
  sidebarLayout(
    sidebarPanel(
    selectInput(inputId = 'From',
              label = 'Wybierz z tabeli',
              choices = c('Seriale','Katalog','Oceny'),
              selected = 'Seriale'),
    selectInput(inputId = 'From2',
                label = 'Sprawdzenie zamówienia',
                choices = c("'Gra o Tron'","'Kompania braci'","'Narcos'","'Dom z papieru'","'Przyjaciele'","'Stranger Things'","'Maniac'","'Seks w wielkim miescie'"),
                selected = 'Gra o Tron')
                
                ),
    
    mainPanel(
                dataTableOutput(outputId = 'first_table'),
                dataTableOutput(outputId ='second_table' )
                )
  )  
)
server <- function(input,output){
  output$first_table <- DT::renderDataTable(dbGetQuery(con,paste0("SELECT * FROM ",input$From,";")))
  output$second_table <- DT::renderDataTable(
    dbGetQuery(con,paste0( 'SELECT * FROM seriale as s
JOIN katalog AS k USING(id_serialu)
                           Join oceny as o ON o.id_serialu = s.id_serialu WHERE s.tytuł =',input$From2,';'))
  )
} 
shinyApp(ui = ui, server = server)

