(function( $ ) {
    var title, authors, price, url,
        loc = document.location;

    title = $( '#btAsinTitle' ).text().replace( /\s\[(Paperback|Hardcover|Bargain Price|Mass Market Paperback)\]/g, '' );

    // authors' names, skip over role e.g. (editor)
    if ( $( '.contributorNameTrigger' )[ 0 ] ) {
        if ( $( '.contributorNameTrigger' ).length > 1 ) {
            authors = $( '.contributorNameTrigger a' )[ 0 ].text();
            for ( var i = 1; i < $( '.contributorNameTrigger' ).length; i++) {
                authors += ', ' + $( '.contributorNameTrigger a' )[ i * 2 ].text();
            }
        } else authors = $( '.contributorNameTrigger a' ).text();
    } else authors = $( '.buying .parseasinTitle ').next().text().replace( /( \(Introduction\))|( \(Foreword\))|( \(Editor\))|( \(Author\))|( \(Translator\))/ig, '' ).trim();

    if ( $( '.priceLarge' ).length > 1 ) {
        // NB: would use $( '.priceLarge' ).last() here
        // but Amazon's jQuery is v. 1.2.6 which doesn't support $().last()
        price = $( '.priceLarge' ).eq( $( '.priceLarge' ).length - 1 ).text();
    } else price = $( '.priceLarge' ).text();

    // leave off query string by combining domain & path
    url = loc.origin + loc.pathname;

    // easiest way to push text into clipboard right now
    prompt( "Press Ctrl+C to copy & then Enter to close this dialog.", title + '\t' + authors + '\t' + price + '\t' + url );
} ( jQuery ));
