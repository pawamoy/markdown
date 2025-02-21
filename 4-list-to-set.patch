diff --git a/markdown/core.py b/markdown/core.py
index 6c7a21b..75f70fc 100644
--- a/markdown/core.py
+++ b/markdown/core.py
@@ -113,7 +113,7 @@ class Markdown:
         ]
         """ List of characters which get the backslash escape treatment. """
 
-        self.block_level_elements: list[str] = BLOCK_LEVEL_ELEMENTS.copy()
+        self.block_level_elements: set[str] = BLOCK_LEVEL_ELEMENTS.copy()
 
         self.registeredExtensions: list[Extension] = []
         self.docType = ""  # TODO: Maybe delete this. It does not appear to be used anymore.
diff --git a/markdown/extensions/md_in_html.py b/markdown/extensions/md_in_html.py
index d1fbd7a..f65a579 100644
--- a/markdown/extensions/md_in_html.py
+++ b/markdown/extensions/md_in_html.py
@@ -42,7 +42,7 @@ class HTMLExtractorExtra(HTMLExtractor):
 
     def __init__(self, md: Markdown, *args, **kwargs):
         # All block-level tags.
-        self.block_level_tags = set(md.block_level_elements.copy())
+        self.block_level_tags = md.block_level_elements.copy()
         # Block-level tags in which the content only gets span level parsing
         self.span_tags = set(
             ['address', 'dd', 'dt', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'legend', 'li', 'p', 'summary', 'td', 'th']
diff --git a/markdown/util.py b/markdown/util.py
index f547721..dfaa3b0 100644
--- a/markdown/util.py
+++ b/markdown/util.py
@@ -44,7 +44,7 @@ Constants you might want to modify
 """
 
 
-BLOCK_LEVEL_ELEMENTS: list[str] = [
+BLOCK_LEVEL_ELEMENTS: set[str] = {
     # Elements which are invalid to wrap in a `<p>` tag.
     # See https://w3c.github.io/html/grouping-content.html#the-p-element
     'address', 'article', 'aside', 'blockquote', 'details', 'div', 'dl',
@@ -56,9 +56,9 @@ BLOCK_LEVEL_ELEMENTS: list[str] = [
     'math', 'map', 'noscript', 'output', 'object', 'option', 'progress', 'script',
     'style', 'summary', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'tr', 'video',
     'center'
-]
+}
 """
-List of HTML tags which get treated as block-level elements. Same as the `block_level_elements`
+Set of HTML tags which get treated as block-level elements. Same as the `block_level_elements`
 attribute of the [`Markdown`][markdown.Markdown] class. Generally one should use the
 attribute on the class. This remains for compatibility with older extensions.
 """
diff --git a/tests/test_apis.py b/tests/test_apis.py
index 55e2cdb..efd6a23 100644
--- a/tests/test_apis.py
+++ b/tests/test_apis.py
@@ -920,7 +920,7 @@ class TestBlockAppend(unittest.TestCase):
     def testBlockAppend(self):
         """ Test that appended escapes are only in the current instance. """
         md = markdown.Markdown()
-        md.block_level_elements.append('test')
+        md.block_level_elements.add('test')
         self.assertEqual('test' in md.block_level_elements, True)
         md2 = markdown.Markdown()
         self.assertEqual('test' not in md2.block_level_elements, True)
