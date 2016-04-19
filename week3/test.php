<?php


$offset = 0;

$list = [];

do {
echo "offset $offset\n";
$data = file_get_contents("http://catalog-service-testing.home24.net/api/v1/articles?appDomain=4&language=de_AT&limit=100&offset={$offset}&fields=sku,minPriceDataRegular");
$data = json_decode($data, true);
$repeat = false;
foreach($data["results"] as $key=>$value){
	if(!isset($value["minPriceDataRegular"])) {
		$sku = $value["sku"];
		$repeat = true;
		echo $value["sku"]."\n";
		
		$delete = "curl http://localhost:9000/solr/catalog_article_4_de_AT/update -H 'Content-type: text/xml' --data-binary '<delete><query>sku:{$sku}</query></delete>'";
		$commit = "curl http://localhost:9000/solr/catalog_article_4_de_AT/update -H 'Content-type: text/xml' --data-binary '<commit />'";
		exec($delete);
		exec($commit);
	}
}
$count = count($data["results"]);
if(!$repeat){
	$offset +=100;
}

sleep(1);
} while ($count > 0);

var_export($list);
