import os
import glob
import urllib.parse
import pandas as pd
import unicodedata

def render_dashboard(readings):


  url1 = get_query_url_for_articles(readings)
  url2 = get_query_url_for_topic_bubble(readings)
  url3 = get_topics_as_table(readings)
  url4 = get_query_url_for_venues(readings)
  url5 = get_query_url_for_locations(readings)
  url6 = get_query_url_for_citing_authors(readings)
  url7 = get_query_url_for_authors(readings)

  html = """


  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Wikidata Bib - Tiago Lubiana</title>
    <meta property="og:description" content="powered by Wikidata">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>
    <body>
    <section class="section">
          <div class="container">
        <div class="columns is-centered">
          <div class="column is-half has-text-centered">
                  <h1 class="title is-1"> My Readings</h1>
              </div>
        </div>
      </div>
      <div class="column is-half has-text-centered">
      </section>
    <div class="container">
        <div class="columns is-centered">
          <div class="column is-half has-text-centered">
            <h4 class="subtitle is-4">
                  Dashboard of Tiago Lubiana's Readings
                  </p>
          </div>
        </div>
    </div>
    </br>
    </br>

  <div role="navigation">
<ul class="nav nav-pills justify-content-center">
  <li class="nav-item">
    <a class="nav-link" aria-current="page" href="/wikidata_bib/">All time</a>
  </li>
    <li class="nav-item">
    <a class="nav-link" href="/wikidata_bib/2020/November.html">November 2020</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/wikidata_bib/2020/December.html">December 2020</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/wikidata_bib/this_week.html">This week</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/wikidata_bib/last_day.html">Last day</a>
  </li>
</ul>
</div>
    </br>
    </br>
        <div class="columns is-centered">
        
            <div class="tabs is-centered">
                <ul>
                    <li id="one-tab" class="">
                        <a onclick="switchToOne()">
                        <span>Articles</span> 
                      </a>
                    </li>
                    <li id="two-tab">
                        <a onclick="switchToTwo()">
                      <span>Topic Bubble</span>
                      </a>
                              </li>
                              <li id="three-tab">
                                  <a onclick="switchToThree()">
                                      <span>Topic Count</span>
                                </a>
                            </li>
                            <li id="four-tab">
                              <a onclick="switchToFour()">
                                  <span>Venues</span>
                            </a>
                        </li>
                        <li id="five-tab">
                          <a onclick="switchToFive()">
                              <span>Author Map</span>
                        </a>
                        <li id="six-tab">
                          <a onclick="switchToSix()">
                              <span>Citing Authors</span>
                        </a>
                        </li> 
                        <li id="seven-tab">
                          <a onclick="switchToSeven()">
                              <span>Authors</span>
                        </a>
                        </li>
                </ul>
                <!--/tabs is-centered-->
            </div>
        </div>
      </div>
      </section>
    <div class="container">
          <div id="one-tab-content">
              <h5 class="title is-5" style="text-align:center;"> What I've been reading </h5>
          <div class="columns is-centered"
            <p style="text-align: center">
              <iframe width=92% height="500" src=""" + '"'+ url1 +'"' + """></iframe>
            </p>
          </div>
            </div>
          <div class="is-hidden" id="two-tab-content">
              <<h5 class="title is-5" style="text-align:center;"> Topics I've been reading in bubbles </h5>
          <div class="columns is-centered"
            <p style="text-align: center">
              <iframe width=92% height="500" src=""" + '"'+ url2 +'"' + """></iframe>
            </p>
          </div>
                  </div>
              <div class="is-hidden" id="three-tab-content">
                      <<h5 class="title is-5" style="text-align:center;"> Topics I've been reading in a table </h5>
                    <div class="columns is-centered"
                        <p style="text-align: center">
                          <iframe width=92% height="500" src=""" + '"'+ url3+'"' + """></iframe>
                        </p>
                    </div>
                    </div>
              <div class="is-hidden" id="four-tab-content">
                      <<h5 class="title is-5" style="text-align:center;">  Which journals I've been reading</h5>
                    <div class="columns is-centered"
                        <p style="text-align: center">
                          <iframe width=92% height="500" src=""" + '"'+ url4 +'"' + """></iframe>
                        </p>
                    </div>
                    </div>
              <div class="is-hidden" id="five-tab-content">
                      <<h5 class="title is-5" style="text-align:center;"> Where are the authors I've been reading </h5>
                    <div class="columns is-centered"
                        <p style="text-align: center">
                          <iframe width=92% height="500" src=""" + '"'+ url5 +'"' + """></iframe>
                        </p>
                    </div>
                    </div>
              <div class="is-hidden" id="six-tab-content">
                      <<h5 class="title is-5" style="text-align:center;"> Who cites what I've been reading </h5>
                    <div class="columns is-centered"
                        <p style="text-align: center">
                          <iframe width=92% height="500" src=""" + '"'+ url6 +'"' + """></iframe>
                        </p>
                    </div>
                    </div>
              <div class="is-hidden" id="seven-tab-content">
                      <<h5 class="title is-5" style="text-align:center;"> Who writes what I've been reading </h5>
                    <div class="columns is-centered"
                        <p style="text-align: center">
                          <iframe width=92% height="500" src=""" + '"'+ url7 +'"' + """></iframe>
                        </p>
                    </div>
                    </div>
      </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script>

      function switchToOne() {
        removeActive();
        hideAll();
        $("#one-tab").addClass("is-active");
        $("#one-tab-content").removeClass("is-hidden");
      }

      function switchToTwo() {
        removeActive();
        hideAll();
        $("#two-tab").addClass("is-active");
        $("#two-tab-content").removeClass("is-hidden");
      }

      function switchToThree() {
        removeActive();
        hideAll();
        $("#three-tab").addClass("is-active");
        $("#three-tab-content").removeClass("is-hidden");
      }

      function switchToFour() {
        removeActive();
        hideAll();
        $("#four-tab").addClass("is-active");
        $("#four-tab-content").removeClass("is-hidden");
      }

      function switchToFive() {
        removeActive();
        hideAll();
        $("#five-tab").addClass("is-active");
        $("#five-tab-content").removeClass("is-hidden");
      }

      function switchToSix() {
        removeActive();
        hideAll();
        $("#six-tab").addClass("is-active");
        $("#six-tab-content").removeClass("is-hidden");
      }

      function switchToSeven() {
        removeActive();
        hideAll();
        $("#seven-tab").addClass("is-active");
        $("#seven-tab-content").removeClass("is-hidden");
      }

      function removeActive() {
        $("li").each(function() {
          $(this).removeClass("is-active");
        });
      }

      function hideAll(){
        $("#one-tab-content").addClass("is-hidden");
        $("#two-tab-content").addClass("is-hidden");
        $("#three-tab-content").addClass("is-hidden");
        $("#four-tab-content").addClass("is-hidden");
        $("#five-tab-content").addClass("is-hidden");
        $("#six-tab-content").addClass("is-hidden");
        $("#seven-tab-content").addClass("is-hidden");
        $("#eight-tab-content").addClass("is-hidden");
      }
    
    </script>
    </br>

  <footer class="footer">
    <div class="container">
      <div class="content has-text-centered">
        <p>
          The content is licensed <a href="https://creativecommons.org/publicdomain/zero/1.0/">under Creative Commons CC0</a>
      
          <p> Wikidata SPARQL Queries adapted from <a href="https://scholia.toolforge.org/">Scholia</a>  </p>
          <p> <strong>Dashboard</strong> adapted by <a href="https://www.wikidata.org/wiki/User:TiagoLubiana">TiagoLubiana</a>
      from the <a href="https://wikiproject-india.github.io/covid19dashboard/">COVID-19 in India dashboard </a>
          <p> To see the links for all notes taken, go to <a href="./notes.html"> this draft page </a>. </p>
        </p>
      </div>
    </div>
  </footer>
  </body>
  </html>
  """
  return(html)

def render_url(query):
  return "https://query.wikidata.org/embed.html#" + urllib.parse.quote(query, safe='')
  
def get_query_url_for_articles(readings):
  query = """

  #defaultView:Table
  SELECT
  (MIN(?dates) AS ?date)
  ?work ?workLabel
  (GROUP_CONCAT(DISTINCT ?type_label; separator=", ") AS ?type)
  (SAMPLE(?pages_) AS ?pages)
  ?venue ?venueLabel
  (GROUP_CONCAT(DISTINCT ?author_label; separator=", ") AS ?authors)
  WHERE {
  VALUES ?work """ +  readings + """.
  ?work wdt:P50 ?author .
  OPTIONAL {
    ?author rdfs:label ?author_label_ . FILTER (LANG(?author_label_) = 'en')
  }
  BIND(COALESCE(?author_label_, SUBSTR(STR(?author), 32)) AS ?author_label)
  OPTIONAL { ?work wdt:P31 ?type_ . ?type_ rdfs:label ?type_label . FILTER (LANG(?type_label) = 'en') }
  ?work wdt:P577 ?datetimes .
  BIND(xsd:date(?datetimes) AS ?dates)
  OPTIONAL { ?work wdt:P1104 ?pages_ }
  OPTIONAL { ?work wdt:P1433 ?venue }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,no,ru,sv,zh". }  
  }
  GROUP BY ?work ?workLabel ?venue ?venueLabel
  ORDER BY DESC(?date)  

  """
  
  return render_url(query)

def get_query_url_for_topic_bubble(readings):

  query = """

  #defaultView:BubbleChart
  SELECT ?score ?topic ?topicLabel
  WITH {
    SELECT
      (SUM(?score_) AS ?score)
      ?topic
    WHERE {
          {
        SELECT (100 AS ?score_) ?topic WHERE {
          VALUES ?work """ +  readings + """.
          ?work  wdt:P921 ?topic . 
        }
      }
      UNION
      {
        SELECT (1 AS ?score_) ?topic WHERE {
          VALUES ?work """ +  readings + """.
          ?citing_work wdt:P2860 ?work .
          ?citing_work wdt:P921 ?topic . 
        }
      }
    }
    GROUP BY ?topic
  } AS %results 
  WHERE {
    INCLUDE %results
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,da,de,es,jp,no,ru,sv,zh". }
  }
  ORDER BY DESC(?score)
  LIMIT 50

  """
  return render_url(query) 

def get_topics_as_table(readings):
  query_3 = """


  #defaultView:Table
  SELECT ?count ?theme ?themeLabel ?example_work ?example_workLabel
  WITH {
    SELECT (COUNT(?work) AS ?count) ?theme (SAMPLE(?work) AS ?example_work)
    WHERE {
      VALUES ?work """ +  readings + """.
      ?work wdt:P921 ?theme .
    }
    GROUP BY ?theme
  } AS %result
  WHERE {
    INCLUDE %result
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh" . } 
  }
  ORDER BY DESC(?count) 

  """
  return render_url(query_3) 

def get_query_url_for_venues(readings):
  query_4 = """


  # Venue statistics for a collection
  SELECT
    ?count (SAMPLE(?short_name_) AS ?short_name)
    ?venue ?venueLabel
    ?topics ?topicsUrl
  WITH {
    SELECT
      (COUNT(DISTINCT ?work) as ?count)
      ?venue
      (GROUP_CONCAT(DISTINCT ?topic_label; separator=", ") AS ?topics)
    WHERE {
      VALUES ?work """ +  readings + """.
      ?work wdt:P1433 ?venue .
      OPTIONAL {
        ?venue wdt:P921 ?topic .
        ?topic rdfs:label ?topic_label . FILTER(LANG(?topic_label) = 'en') }
    }
    GROUP BY ?venue
  } AS %result
  WHERE {
    INCLUDE %result
    OPTIONAL { ?venue wdt:P1813 ?short_name_ . }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh". }  
  } 
  GROUP BY ?count ?venue ?venueLabel ?topics ?topicsUrl
  ORDER BY DESC(?count)

  """
  return render_url(query_4) 

def get_query_url_for_locations(readings):
  query_5 = """


  #defaultView:Map
  SELECT ?organization ?organizationLabel ?geo ?count ?layer
  WITH {
    SELECT DISTINCT ?organization ?geo (COUNT(DISTINCT ?work) AS ?count) WHERE {
      VALUES ?work """ +  readings + """.
          ?work wdt:P50 ?author .
      ?author ( wdt:P108 | wdt:P463 | wdt:P1416 ) / wdt:P361* ?organization . 
      ?organization wdt:P625 ?geo .
    }
    GROUP BY ?organization ?geo ?count
    ORDER BY DESC (?count)
    LIMIT 2000
  } AS %organizations
  WHERE {
    INCLUDE %organizations
    BIND(IF( (?count < 1), "No results", IF((?count < 2), "1 result", IF((?count < 5), "1 < results ≤ 10", IF((?count < 101), "10 < results ≤ 100", IF((?count < 1001), "100 < results ≤ 1000", IF((?count < 10001), "1000 < results ≤ 10000", "10000 or more results") ) ) ) )) AS ?layer )
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }        
  }
  ORDER BY DESC (?count)


  """
  return render_url(query_5)

def get_query_url_for_citing_authors(readings):
  query_6 = """


  #defaultView:Table
  SELECT
    ?count
    ?citing_author ?citing_authorLabel

    # Either show the ORCID iD or construct part of a URL to search on the ORCID homepage
    (COALESCE(?orcid_, CONCAT("orcid-search/quick-search/?searchQuery=", ENCODE_FOR_URI(?citing_authorLabel))) AS ?orcid)
  WITH {
    SELECT (COUNT(?citing_work) AS ?count) ?citing_author WHERE {
      VALUES ?work """ +  readings + """.
      ?citing_work wdt:P2860 ?work . 
      ?citing_work wdt:P50 ?citing_author .
    }
    GROUP BY ?citing_author 
    ORDER BY DESC(?count)
    LIMIT 500
  } AS %counts
  WITH {
    # An author might have multiple ORCID iDs
    SELECT
      ?count
      ?citing_author
      (SAMPLE(?orcids) AS ?orcid_)
    WHERE {
      INCLUDE %counts
      OPTIONAL { ?citing_author wdt:P496 ?orcids }
    }
    GROUP BY ?count ?citing_author
  } AS %result
  WHERE {
    INCLUDE %result

    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh". }
  } 
  ORDER BY DESC(?count)


  """
  return render_url(query_6)

def get_query_url_for_authors(readings):
  query_7 = """
  #defaultView:Table
  SELECT (COUNT(?work) AS ?count) ?author ?authorLabel ?orcids  WHERE {
    VALUES ?work """ +  readings + """.
    ?work wdt:P50 ?author .
      OPTIONAL { ?author wdt:P496 ?orcids }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh". }

    }
  GROUP BY ?author ?authorLabel ?orcids 
  ORDER BY DESC(?count)

  """
  return render_url(query_7)
