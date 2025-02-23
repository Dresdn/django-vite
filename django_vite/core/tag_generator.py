from typing import Dict, Optional

Tag = str


def attrs_to_str(attrs: Dict[str, str]):
    """
    Convert dictionary of attributes into a string that can be injected into a <script/>
    tag.
    """
    attrs_str = " ".join(
        [f'{key.replace("_", "-")}="{value}"' for key, value in attrs.items()]
    )
    return attrs_str


class TagGenerator:
    @staticmethod
    def script(src: str, attrs: Dict[str, str]) -> Tag:
        """
        Generates an HTML script tag.

        Arguments:
            src {str} -- Source of the script.

        Keyword Arguments:
            attrs {Dict[str, str]} -- List of custom attributes
                for the tag.

        Returns:
            str -- The script tag.
        """

        attrs_str = attrs_to_str(attrs)

        return f'<script {attrs_str} src="{src}"></script>'

    @staticmethod
    def stylesheet(href: str, attrs: Optional[Dict[str, str]] = None) -> Tag:
        """
        Generates an HTML <link> stylesheet tag for CSS.

        Arguments:
            href {str} -- CSS file URL.

        Returns:
            str -- CSS link tag.
        """

        attrs_str = attrs_to_str(attrs if attrs else {})

        return f'<link {attrs_str} rel="stylesheet" href="{href}" />'

    @staticmethod
    def stylesheet_preload(href: str, attrs: Optional[Dict[str, str]] = None) -> Tag:
        """
        Generates an HTML <link> preload tag for CSS.

        Arguments:
            href {str} -- CSS file URL.

        Returns:
            str -- CSS link tag.
        """

        attrs_str = attrs_to_str(attrs if attrs else {})

        return f'<link {attrs_str} rel="preload" href="{href}" as="style" />'

    @staticmethod
    def preload(href: str, attrs: Dict[str, str]) -> Tag:
        attrs_str = attrs_to_str(attrs)

        return f'<link href="{href}" {attrs_str} />'
