<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns="http://www.w3.org/1999/xhtml" 
								xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output method="html" indent="yes"/>  

	<xsl:include href="main.xslt"/>

	<xsl:template match="/">
		<xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html></xsl:text>
		<html lang="en">
			<head>
				<title>mwil.me</title>

				<meta charset="utf-8"/>
				<meta name="viewport" content="width=device-width, initial-scale=1"/>
			
				<link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.css"/>
				<link rel="stylesheet" href="me.css"/>

				<script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
				<script src="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.js"></script>

				<script src="src/me.js"></script>
			</head>

			<body>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="page">
		<div data-role="page" id="{@id}">
			<div data-role="content">
				<xsl:apply-templates/>
			</div>
		</div>
	</xsl:template>

	<!-- do nothing for unmatched text or attribute nodes -->
	<xsl:template match="text()|@*"/>

</xsl:stylesheet>
