window.jQuery || document.write('<script src="/static/js/jquery.min.js"><\/script>');
$(function () {
    "use strict";

});


                        var $buoop = {};
                        $buoop.ol = window.onload;
                        window.onload = function () {
                            try {
                                if ($buoop.ol) $buoop.ol();
                            } catch (e) {
                            }
                            var e = document.createElement("script");
                            e.setAttribute("type", "text/javascript");
                            e.setAttribute("src", "http://browser-update.org/update.js");
                            document.body.appendChild(e);
                        }
                    