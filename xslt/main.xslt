<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns="http://www.w3.org/1999/xhtml" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="mw-summary">
		<h1><xsl:text>Matthias Wilhelm</xsl:text></h1>

		<p><xsl:text>I'm currently a Ph.D. student in the Department of Computer Science at the Technical University of Kaiserslautern, Germany, supervised by Jens B. Schmitt.</xsl:text></p>
		<p><xsl:text>I'm interesting in physical layer security mechanisms, software-defined radio technology, and the effects of interference and jamming on wireless communications.</xsl:text></p>
	</xsl:template>

	<xsl:template match="project-summary">
		<xsl:text disable-output-escaping='yes'>&lt;br /></xsl:text>
		<h2><xsl:text>List of Research Projects</xsl:text></h2>
		<xsl:copy-of select="document('../xml/project-summary.xml')" />
	</xsl:template>

	<xsl:template match="publications">
		<xsl:text disable-output-escaping='yes'>&lt;br /></xsl:text>
		<h2><xsl:text>List of Publications</xsl:text></h2>
		<xsl:copy-of select="document('../xml/pubs.xml')" />
	</xsl:template>

	<xsl:template match="cv-items">
		<xsl:text disable-output-escaping='yes'>&lt;br /></xsl:text>
		<h2><xsl:text>Random CV Items</xsl:text></h2>
		<xsl:copy-of select="document('../xml/cv.xml')" />
	</xsl:template>

	<xsl:template match="contact">
		<xsl:text disable-output-escaping='yes'>&lt;br /></xsl:text>
		<h2><xsl:text>Contact</xsl:text></h2>
		<xsl:copy-of select="document('../xml/contact.xml')" />
	</xsl:template>

	<xsl:template match="bibtex-popup">
		<div data-role="popup" data-rel="back" data-position-to="window" data-transition="pop" class="ui-content" id="bibtex-popup">
			<a href="#" data-rel="back" data-role="button" data-theme="c" data-icon="delete" data-iconpos="notext" class="ui-btn-right">
				<xsl:text>Close</xsl:text>
			</a>
			<h4><xsl:text>BibTeX entry:</xsl:text></h4>

			<form>
				<textarea cols="120" rows="8" id="bibtex-textarea" />
			</form>
		</div>
	</xsl:template>

</xsl:stylesheet>
