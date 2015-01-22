wrbt-poc
====

This is a proof of concept implementation of [wrbt](https://github.com/benhylau/wrbt) where `scheme://host` is chosen to be `http://wrbt-poc.appspot.com`. This implementation aims to facilitate peering in three specific use cases. First of all, let's assume the following peering request is sent through an insecure channel, whether that be direct email or some broadcasted channel like a Tweet.

http://wrbt-poc.appspot.com/?type=peer&protocol=UDPInterface&pk=wrbtPk&metadata=metadataOfAlice&cjdnsVersion=X&wrbtVersion=Y

### Case 1

The receiver of this peering request clicks on the message from a desktop. The `http://wrbt-poc.appspot.com` back-end, currently deployed on Google App Engine, redirects the user to Hyperboria as a welcome screen. Try clicking on it.

### Case 2

The receiver clicks from an Android phone without the [cjdns app](https://github.com/BerlinMeshnet/cjdns-android) installed. The phone launches the peering request as a URL in the browser, which the Python back-end detects as an Android device from the User Agent, and redirects with a `market://details?id=cjdns.android.package.name` URI causing the phone to launch the app install page from the native Google Play app. I have directed to an in-market app for now, but you get the idea. Try clicking on the peering request from your Android phone.

### Case 3

The receiver clicks from an Android phone with the [cjdns app](https://github.com/BerlinMeshnet/cjdns-android) installed. This means the user is already on Hyperboria and is in a position to peer with the requester. The cjdns app advertises itself to handle `http://wrbt-poc.appspot.com`, so it [presents itself to handle this URI](https://github.com/benhylau/cjdns-android/pull/1). Upon selecting the cjdns app, the user will be presented with a dialog, and can choose to offer peering to the requester. Then the rest will proceed as described in [wrbt](https://github.com/benhylau/wrbt).