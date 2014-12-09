// ==UserScript==
// @name       Ref Analytics validation
// @namespace  http://faq.chesapeake.edu/record.php
// @version    0.1
// @description  Enforce data consistency when filling in reference transactions.
// @match      http://faq.chesapeake.edu/record.php
// @copyright  CC0 Public Domain
// ==/UserScript==
(function( $ ) {
    var $mode = $( '#metadata1' ),
      $type = $( '#metadata2' ),
      $dirType = $( '#metadata3' ),
      $subject = $( '#metadata4' ),
      $techTopic = $( '#metadata5' ),
      errors = [];

    // if cond is false, push msg to error list & execute callback
    function test ( cond, msg, cb ) {
      if ( !cond ) {
        errors.push( msg );
        if ( cb ) cb();
      }
    }

    // given jQuery object, return selected child <option>
    function sel ( jq ) {
      return jq.find( 'option:selected' );
    }

    function highlight ( jq ) {
      return jq.find( '.ftitle' ).addClass( 'err' );
    }

    function clearHighlights () {
      $( '.ftitle' ).removeClass( 'err' );
    }

    // enforce required fields globally & for specific types
    function requirements () {
      // make mode & type required for all
      test( sel( $mode ).length,
        'Communication mode is required for each interaction.',
        function () { highlight( $mode ); } );
      test( sel( $type ).length,
        'Type is required for each interaction.',
        function () { highlight( $type ); } );

      // Directional Type is required for Type == Directional
      if ( sel( $type ).text().match( 'Directional' ) ) {
        test( sel( $dirType ).length,
          'Every Directional question must have a Directional Type.',
          function () { highlight( $dirType ); } );
      }
      // Tech Topic is required for every Type == Computer Help
      if ( sel( $type ).text().match( 'Computer Help' ) ) {
        test( sel( $techTopic ).length,
          'Every Computer Help question must have a Tech Topic.',
          function () { highlight( $techTopic ); } );
      }
    }

    // someone's filled out something inappropriate for the type
    function inverseRequirements () {
      // Directionals shouldn't have a Subject or Tech Topic
      if ( sel( $type ).text().match( 'Directional' ) ) {
        test( !sel( $subject ).length,
          'Directionals cannot have a Subject. It has been unselected.',
          function () { $subject.find( 'a' ).click(); } );
        test( !sel( $techTopic ).length,
          'Directionals cannot have a Tech Topic. It has been unselected.',
          function () { $techTopic.find( 'a' ).click(); } );
      }

      // Computer Help shouldn't have a Directional Type or Subject
      if ( sel( $type ).text().match( 'Computer Help' ) ) {
        test( !sel( $subject ).length,
          'Computer Help cannot have a Subject. It has been unselected.',
          function () { $subject.find( 'a' ).click(); } );
        test( !sel( $dirType ).length,
          'Computer Help cannot have a Directional Type. It has been unselected.',
          function () { $dirType.find( 'a' ).click(); } );
      }

      // Reference shouldn't have a Directional Type or Tech Topic
      if ( sel( $type ).text().match( 'Reference' ) ) {
        test( !sel( $techTopic ).length,
          'Reference cannot have a Tech Topic. It has been unselected.',
          function () { $techTopic.find( 'a' ).click(); } );
        test( !sel( $dirType ).length,
          'Reference cannot have a Directional Type. It has been unselected.',
          function () { $dirType.find( 'a' ).click(); } );
      }
    }

    // run all the validation, alert any errors
    function validate ( event ) {
      var clear = 0,
        btnText = $( this ).text();

      // clear previously-highlighted errors
      clearHighlights();
      // error checking
      requirements();
      inverseRequirements();

      if ( errors.length === 0 ) {
        clear = ( btnText === 'Submit' ? 0 : 1 );
        // SpringShare function, 0 submits & 1 clears, too
        recordQ( clear );
      } else {
        // there's at least 1 error, alert 'em all
        alert( errors.join( '\n' ) );
        // clear the list or we'll see duplicates next time around
        errors = [];
      }

    }

    // set up .err class used in highlighting
    $( 'body' ).append( '<style> .err { background: rgba( 252, 67, 67, .6 ); color: black; } </style>' );
    $( '#submitdiv button' ).on( 'click', validate );
    // remove handlers from Submit buttons, will fire these manually in validate()
    $( '#submitdiv button' ).removeAttr( 'onclick' );

} ( jQuery ));
