"""Create an asset given url to Archivist and user Token.

The module contains two functions: main and create_asset. Main function parses in
a url to the Archivist and a token, which is a user authorization.
The main function would initialize an archivist connection using the url and
the token, called "arch", then call arch.assets.create() and the asset will be created.
"""

from archivist.archivist import Archivist


def create_asset(arch):
    """Create an asset using Archivist Connection.

    Args:
        arch: archivist connection.

    Returns:
        newasset: a new asset created.

    """
    attrs = {
        "arc_display_name": "display_name",  # Asset's display name in the user interface
        "arc_description": "display_description",  # Asset's description in the user interface
        "arc_display_type": "desplay_type",  # Arc_display_type is a free text field
        # allowing the creator of
        # an asset to specify the asset
        # type or class. Be careful when setting this:
        # assets are grouped by type and
        # sharing policies can be
        # configured to share assets based on
        # their arc_display_type.
        # So a mistake here can result in asset data being
        # under- or over-shared.
        "some_custom_attribute": "value"  # You can add any custom value as long as
        # it does not start with arc_
    }
    behaviours = [
        "Attachments",
        "Firmware",
        "LocationUpdate",
        "Maintenance",
        "RecordEvidence",
    ]

    # The first argument is the behaviours of the asset
    # The second argument is the attributes of the asset
    # The third argument is wait for confirmation:
    #   If @confirm@ is True then this function will not
    #   return until the asset is confirmed on the blockchain and ready
    #   to accept events (or an error occurs)
    #   After an asset is submitted to the blockchain (submitted),
    #   it will be in the "Pending" status.
    #   Once it is added to the blockchain, the status will be changed to "Confirmed"
    return arch.assets.create(behaviours, attrs=attrs, confirm=True)


def main():
    """Main function of create asset.

    Parse in user input of url and auth token and use them to
    create an example archivist connection and create an asset.

    """
    with open(".auth_token", mode="r") as tokenfile:
        authtoken = tokenfile.read().strip()

    # Initialize connection to Archivist
    arch = Archivist(
        "https://rkvst.poc.jitsuin.io",
        auth=authtoken,
    )
    # Create a new asset
    asset = create_asset(arch)
    print("Asset", asset)


if __name__ == "__main__":
    main()
