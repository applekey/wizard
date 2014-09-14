/*
 * @name wowBook
 *
 * @author Marcio Aguiar
 * @version 1.0
 * @requires jQuery v1.7.0
 *
 * Copyright 2010 Marcio Aguiar. All rights reserved.
 *
 * To use this file you must to buy a license at http://codecanyon.net/user/maguiar01/portfolio
 *
 * Date: Wed Dec 8 10:05:49 2010 -0200
 */
;(function($) {

$.wowBook = function(elem){
    return $(elem).data("wowBook");
};

$.wowBook.support = {};

$.fn.wowBook = function(options) {
	if (typeof options==="string") {
		var args = Array.prototype.slice.call( arguments, 1 );
		if (options==="options" || options==="prop") {
			var instance = $.wowBook(this[0]), attr=args[0];
			return args.length>1 ?
				instance[attr] = args[1]
			  : instance[attr];
		}
		return this.each(function() {
			var instance = $.wowBook(this),
			    what = instance[options];
			what.apply(instance, args);
		});
	}
    var	opts = $.extend({}, $.wowBook.defaults, options);
	return this.each(function() {
        var book  = new wowBook(this, opts);
		$(this).data('wowBook', book);
	});
}; // fn.wowBook



//
// Book constructor
//
// params:
//  elem - the DOM element that contains the book pages
//  opts - configuration options
//
function wowBook(elem, opts) {
	elem = $(elem);
    var book = this;
    this.elem   = elem;
	this.id     = elem.attr('id');
    this.pages  = [];
    this.opts   = opts;
    this.currentPage = null;
    this.pageWidth   = opts.width/2;
    this.pageHeight  = opts.height;
	this.startPage   = opts.startPage;
	this.onShowPage  = opts.onShowPage;
	this.slideShow   = opts.slideShow;
	this.slideShowDelay   = opts.slideShowDelay;
	this.pauseOnHover     = opts.pauseOnHover;
	this.turnPageDuration = opts.turnPageDuration;
	this.foldGradient     = opts.foldGradient;
	this.foldGradientThreshold = opts.foldGradientThreshold;
	this.shadows          = opts.shadows;
	this.shadowThreshold   = opts.shadowThreshold;
	this.clipBoundaries   = opts.clipBoundaries;
	this.zoomLevel        = 1;
	this.zoomMax          = opts.zoomMax;
	this.zoomMin          = opts.zoomMin;
	this.zoomBoundingBox  = opts.zoomBoundingBox;
	this.zoomStep         = opts.zoomStep;
	this.onZoom           = opts.onZoom;
	this.mouseWheel       = opts.mouseWheel;
	this.flipSound        = opts.flipSound;
	this.centeredWhenClosed = opts.centeredWhenClosed;
	this.sectionDefinition = opts.sections;
	this.rtl              = !!opts.rtl;
	$.wowBook.support.filters = 'filters' in elem[0];

	var pageWidth=this.pageWidth, pageHeight=this.pageHeight;

	// setup element css
	elem.addClass('wowbook');
	if (elem.css('position')==='static') elem.css('position', 'relative');

	var pages = elem.children();
	if ( pages.length < opts.pageCount ) {
		var i = opts.pageCount-pages.length;
		while(i--){ elem.append("<div />"); }
		pages = elem.children();
	}

	// page Container
	var container =
	this.pagesContainer =
	this.origin = $("<div class='wowbook-origin'></div>").css({
		position : 'absolute'
	}).appendTo(elem);

	// Book Shadow element
	book.bookShadow = $("<div class='wowbook-book-shadow'></div>").appendTo(elem)
		.css({ top:0, position: 'absolute', display: 'none', zIndex: 0 });

	// find and Add pages
	this.insertPages(pages, true);

	//
	// create shadows and gradients
	//
	container.append("<div class='wowbook-shadow-clipper'><div class='wowbook-shadow-container'><div class='wowbook-shadow-internal'></div></div></div>");
	book.shadowContainer = $(".wowbook-shadow-container", container);
	book.internalShadow = $(".wowbook-shadow-internal", container);
	book.shadowClipper = $(".wowbook-shadow-clipper", container).css({ display:'none' });
	book.foldShadow = $("<div class='wowbook-shadow-fold'></div>").appendTo(book.shadowContainer);
	book.foldGradientContainer = $("<div class='wowbook-fold-gradient-container'></div>").appendTo(book.shadowContainer);
	book.foldGradientElem  = $("<div class='wowbook-fold-gradient'></div>").appendTo(book.foldGradientContainer);
	book.hardPageShadow = $("<div class='wowbook-hard-page-shadow'></div>")
		.css({ display: 'none' })
		.appendTo(container);
	if (!$.support.opacity && $.wowBook.support.filters) {
		$.wowBook.applyAlphaImageLoader(["wowbook-fold-gradient", "wowbook-fold-gradient-flipped", "wowbook-shadow-fold", "wowbook-shadow-fold-flipped"]);
	}
	// for IE : without this the child elements (shadows) inside the container ignores the parent's opacity
	book.shadowContainer.css('position', 'relative');

    // create handles over the book
	this.leftHandle  = $("<div class='wowbook-handle wowbook-left'></div>")
		.data('corner', 'l').appendTo(container);
	this.rightHandle = $("<div class='wowbook-handle wowbook-right'></div>")
		.data('corner', 'r').appendTo(container);

	// Mac's Safari 4 (probably until 5.0.5) does not accepts transform perspective with unit
	if (Modernizr.csstransforms3d){
		var dummy = $("<div>").css('transform', 'perspective(1px)')
		this.perspectiveUnit = (dummy.css('transform')!="none") ? "px" : ""
		dummy = null
	}


	// in IE, the z-index of the empty transparent divs used to
	// define the handles are ignored if any other element is on front of them
	// the OMG-I-HATE-IE solution is to make them no-transparent, but opacity=1
	if ($.browser.msie)
		$('.wowbook-handle', elem).css({
			backgroundColor: '#fff',
			opacity: '0.01'
		})

	// drag a handle, hold page
	$('.wowbook-handle', container).bind('mousedown.wowbook', function(e){ return book.pageEdgeDragStart(e) });

	// Curl page corner on hover
	if (opts.curl) {
		$('.wowbook-handle', container).hover(function(e){
			if (book.curlTimer) return;
			var page   = (this==book.leftHandle[0]) ? book.leftPage() : book.rightPage()
			if (!page) return
			var offset = page.offset(),
			    x = e.pageX - offset.left,
			    y = e.pageY - offset.top;
			book.curlTimer = setTimeout(function(){
				book.curl(page, y>book.pageHeight/2 )
			}, 120 )
		}, function(){
			book.curlTimer = clearTimeout( book.curlTimer )
			book.uncurl()
		});
	}

	// short-click a handle, turn page
	var mousedownAt, corner;
	$('.wowbook-handle', container)
		.on("mousedown.wowbook", function(){ mousedownAt = $.now(); corner=$(this).data('corner'); })
		.on("mouseup.wowbook", function(){
			var g = $(this).data('corner');
			var clickDuration = new Date().getTime()-mousedownAt;
			if (clickDuration>book.opts.handleClickDuration || g!=corner) return;
			book.stopAnimation();
			if (g==='r') book[book.rtl ? "back" : "advance"]();
			if (g==='l') book[book.rtl ? "advance" : "back"]();
			corner="";
		});

	// 	slideshow pauseOnHover
	var slideShowRunning = false;
	elem.hover(function(e){
		if (!book.pauseOnHover) return;
		slideShowRunning = book.slideShowTimer;
		var ssc = $(book.opts.controls.slideShow),
		    disabled = ssc.hasClass('wowbook-disabled');
		book.stopSlideShow();
		ssc.toggleClass('wowbook-disabled', disabled);
	}, function(){
		if (!book.pauseOnHover) return;
		if (slideShowRunning) book.startSlideShow();
	});

	// Clip Boundaries
	if (this.clipBoundaries) {
		this.origin.wrap("<div class='wowbook-clipper'><div class='wowbook-inner-clipper'></div></div>")
		$(".wowbook-inner-clipper", elem).css({
			position : 'absolute',
			width    : '100%',
			overflow : 'hidden'
		});
		this.clipper = $(".wowbook-clipper", elem).css({
			position: 'absolute', left:0, top:0, width:'100%',
			overflow: 'hidden', zIndex: 1
		});
	}


	// Zoom
	elem.wrapInner("<div class='wowbook-zoomwindow'><div class='wowbook-zoomcontent'></div></div>");
	this.zoomWindow  = $('.wowbook-zoomwindow', elem);
	this.zoomContent = $('.wowbook-zoomcontent', elem);
	if ($.browser.ie8mode) this.zoomContent.wrapInner("<div class='IE8-zoom-helper'style='position:relative'></div>");
	this.zoomWindow.css({
		position : 'absolute',
		top      : 0
	});
	this.zoomContent.css({
		position : 'absolute',
		left     : 0,
		top      : 0
	});
	this.zoomSetup();

	this.setDimensions(this.opts.width, this.opts.height);
	if (opts.scaleToFit) {
		this.scaleToFit();
		this.responsive();
	}


	this.fillToc();

	// Use translate3d ?
	var useTranslate3d = opts.useTranslate3d;
	if (Modernizr.csstransforms3d && useTranslate3d){
		$.wowBook.useTranslate3d = (useTranslate3d == true) ||
		                          ((useTranslate3d == 'mobile') && $.wowBook.utils.isMobile());
	}
	opts.useScale3d = opts.useScale3d && Modernizr.csstransforms3d;


	// deep linking
	if (opts.deepLinking && this.getLocationHash()) {
		var page;
		try { page = book.selectorToPage('#'+this.getLocationHash()); } catch(e){}

		if (page===undefined) page=book.locationHashToPage();
		if (typeof(page)==='number') {
			book.startPage = page;


			if (!isInViewPort(book.elem)) book.elem[0].scrollIntoView();
		}
	}

	// Page flipping sound
	if (this.flipSound) this.audio = this.createAudioPlayer();

	// Keyboard navigation
	if (this.opts.keyboardNavigation) {
		$(document).on("keydown.wowbook", function(e){
			// ignore when typing in a input element
			if ($(e.target).filter('input, textarea, select').length) return;
			if (e.which===book.opts.keyboardNavigation.back) book.back();
			if (e.which===book.opts.keyboardNavigation.advance) book.advance();
		});
	}

	$(window).on("hashchange.wowbook",function(){
		var locationHash = window.location.hash;
		if (locationHash===book.locationHashSetTo) {
			book.locationHashSetTo = undefined;
			return;
		}
		// true if location.hash is empty and does not have even a "#" sign
		var emptyHash = (locationHash==='' && !book.locationEndsInHash());
		var page = emptyHash ? book.startPage : book.locationHashToPage();
		if (typeof(page)!=='number') return;
		book.gotoPage(page, !emptyHash);
		if (!emptyHash && !isInViewPort(book.elem)) book.elem[0].scrollIntoView();
	});

	// forceBasicPage
	if (opts.forceBasicPage) {
		this.foldPage = this.holdHardpage = this.foldPageBasic;
	}

	if (!$.wowBook.support.transform) {
		this.foldPage = this.foldPageBasic;
		if (!$.wowBook.support.filters) this.holdHardpage = this.foldPageBasic;
	}

	// Mouse wheel support
	if (this.mouseWheel) {
		if (book.mouseWheel=="zoom"){
			elem.bind("mousemove.wowbook mouseenter.wowbook", function(event){
				book._mousemoveEvent = event;
			})
		}
		elem.mousewheel(function(e, delta) {
			if (!book.mouseWheel) return;
			if (book.mouseWheel==='zoom') {
				var o = book.elem.offset(),
				    event = book._mousemoveEvent,
				    x = event.pageX-o.left,
				    y = event.pageY-o.top;
				if (delta>0) book.zoomIn({x: x, y: y});
				if (delta<0) book.zoomOut({x: x, y: y});
			} else {
				if (delta>0) book.advance();
				if (delta<0) book.back();
			}
			return false;
		});
	}

	if (this.opts.touchEnabled) this.touchSupport();

	// Turns elements into controls
	this.controllify(this.opts.controls);


	if (this.opts.thumbnails) this.createThumbnails()
	this.setupFullscreen();

	this.showPage(this.startPage, false);
	if (this.opts.zoomLevel!=1) this.zoom(this.opts.zoomLevel, {duration: 0});

	// raf
	this.callRAFCallback = function(){ book.rafCallback() };
	window.raf(this.callRAFCallback);

	if (opts.slideShow) this.startSlideShow();
}// wowBook

// wowBook methods
wowBook.prototype = {



	destroy : function(){
		this.callRAFCallback = $.noop;
		this.curlTimer = clearTimeout( this.curlTimer )
		$("*").add(document).add(window).off(".wowbook");
		this.destroyThumbnails();
		this.stopSlideShow();
		this.stopAnimation(false)
		this.elem.empty().removeData().off()
	} // destroy

	,setDimensions : function(awidth, aheight){
		if (this.zoomed) this.zoom(1);
		this.currentScale = 1;

		var elem = this.elem;
		var oldPageWidth = this.pageWidth;

		elem.css({
			height : aheight,
			width  : awidth
		});

		var elemHeight = elem.height();
		this.pageWidth  = elem.width()/2;
		this.pageHeight = elemHeight;

		if (!this._originalHeight) this._originalHeight = this.pageHeight;
		if (!this._originalWidth)  this._originalWidth = this.pageWidth*2;


		// page Container
		var container = this.origin.css({
			width  : '100%',
			height : elemHeight
		})
		if (oldPageWidth && this.centeredWhenClosed) {
			var left = parseFloat(container.css('left'), 10);
			container.css('left', left/(oldPageWidth/this.pageWidth));
		}

		this.bookShadow.css({ width: awidth, height: aheight });

		var content;
		for(var i=0,l=this.pages.length;i<l;i++){
			this.pages[i].css({
				width: this.pageWidth,
				height: this.pageHeight,
				left: this.pages[i].onLeft ? 0 : this.pageWidth
			});
			content = $('.wowbook-page-content', this.pages[i]);
			boxSizingBorderBox(content, this.pageWidth, this.pageHeight);
		}

		if (this.opts.gutterShadow) {
			$('.wowbook-gutter-shadow', elem).css('height', this.pageHeight); // on IE7, if page content has padding the height 100% will not cover all the pageHeight
		}

		this.positionBookShadow();

		this.shadowClipper.css({ width: elem.width(), height: elemHeight });
		this.hardPageShadow.css({ width: this.pageWidth, height: this.pageHeight })

		if (this.opts.handleWidth) $('.wowbook-handle', container).css('width', this.opts.handleWidth);
		// for some reason IE8 makes this handle disappear when zoomed if we set css 'right:0', so...
		this.rightHandle.css('left', awidth-this.rightHandle.width() );

		// Clip Boundaries
		if (this.clipBoundaries) {
			var pageDiagonal = Math.ceil(Math.sqrt(this.pageWidth*this.pageWidth+this.pageHeight*this.pageHeight)),
				boundaries   = [this.pageHeight-pageDiagonal, elem.width(), pageDiagonal, 0]; // top, right, bottom, left
			this.origin.css('top', -boundaries[0]);
			$(".wowbook-inner-clipper", elem).css({
				width    : '100%',
				height   : boundaries[2]-boundaries[0],
				top      : boundaries[0]
			});
			this.clipper.css({ width:'100%', height: elemHeight });
		}

		// Zoom
		this.zoomWindow.css({
			width    : this.pageWidth*2,
			height   : elemHeight
		});
		this.zoomContent.css({
			width    : this.pageWidth*2,
			height   : elemHeight
		});

		// page corners
		this.corners = {
			tl : [0, 0],
			bl : [0, this.pageHeight],
			tr : [this.pageWidth, 0],
			br : [this.pageWidth, this.pageHeight],
			l  : [0, 0],
			r  : [this.pageWidth, 0]
		};

		if (this.thumbnails) this.updateThumbnails();
	}, // setDimensions


	scale : function(factor){
		if (!$.wowBook.support.transform) return;
		if (this.zoomed) this.zoom(1, 0, { offset: { dx:0, dy: 0 }})
		this.currentScale = factor;
		var container = this.zoomContent;

		if (this.opts.zoomUsingTransform) {
			container.css({
				transform: "scale("+factor+")"
				,transformOrigin : "0 0"
			})
		} else {
			container.css('zoom', factor);
			this._cssZoom = factor*this.zoomLevel;
		}
		this.elem.css({
			height : this._originalHeight*factor,
			width  : this._originalWidth*factor
		});






		if (this.opts.onResize) this.opts.onResize(this)
	}, // scale










	scaleToFit : function(widthOrSelector, height){
		var width = widthOrSelector;
		if (!$.isNumeric(widthOrSelector)) {
			var container = $(widthOrSelector || this.opts.scaleToFit);
			if (!container.length) throw "jQuery selector passed to wowbook.resize did not matched in any DOM element."
			width  = container.width();
			height = container.height();
		}
		var ar = this._originalWidth/this._originalHeight;
		if (height*ar<=width) width=height*ar
		else height = width/ar;
		this.scale(height/this._originalHeight)
	}, // scaleToFit

	resize : function(width, height){




		this.setDimensions(width, height);
		if (this.opts.onResize) this.opts.onResize(this)
	}, // resize

	responsive : function(){
		var book=this;
		$(window).on("resize.wowbook", function(){
			book.scaleToFit()
		})
	}, // responsive

	/*
	 * Insert pages in the book
	 */
	insertPages : function(pages, dontShowPage){
		for(var i=0,l=pages.length;i<l;i++){
			this.insertPage(pages[i], true);
		};
		this.updateBook(dontShowPage);
	},

	/*
	 * Insert a single page in the book
	 *
	 * 	content - the page content, can be a string or a jquery object
	 *  dontUpdateBook - boolean, if true updateBook will NOT be called updateBook after the insert.
	 *                   Use this if you're insert several pages in batch, and call updateBook after.
	 */
	insertPage : function(content, dontUpdateBook){
		if ( this.isDoublePage(content) ) {
			this.insertDoublePage( content, dontUpdateBook )
			return
		}
		var index=this.pages.length;
		content = $(content).addClass('wowbook-page-content');
		var page = $("<div class='wowbook-page'></div>")
		       .css({ width: this.pageWidth, height: this.pageHeight, display : 'none', position : 'absolute' })
		       .appendTo(this.pagesContainer)
		       .append(content);
		if ($.wowBook.support.boxSizing) content.css($.wowBook.support.boxSizing, 'border-box');
		boxSizingBorderBox(content, this.pageWidth, this.pageHeight);
		page.hardPageSetByUser = content.hasClass('wowbook-hardpage');
		if (this.opts.gutterShadow) {
			$("<div class='wowbook-gutter-shadow'></div>")
				.appendTo(content).css('height', this.pageHeight); // on IE7, if page content has padding the height 100% will not cover all the pageHeight
		}
		this.pages.push(page);

		if (!dontUpdateBook) this.updateBook();

		return page;
	}, // insertPage

	insertDoublePage : function(content, dontUpdateBook){
		if (this._insertingDoublePage) return;
		this._insertingDoublePage = true;

		var leftHalf  = $(content),
		    rightHalf = leftHalf.clone().insertAfter(leftHalf),
		    whole     = leftHalf.add(rightHalf);
		leftHalf.css('left', 0);
		rightHalf.css('right', '100%');
		whole.css({
			width: "200%",
			height: "100%",
			position: "relative"
		});
		whole.css($.wowBook.support.boxSizing+"", 'border-box')
		     .wrap("<div class='wowbook-double-page'></div>");

		this.insertPage(leftHalf.parent(), true);
		this.insertPage(rightHalf.parent(), true);
		if (!$.wowBook.support.boxSizing) {
			boxSizingBorderBox(leftHalf, this.pageWidth*2, this.pageHeight);
			boxSizingBorderBox(rightHalf, this.pageWidth*2, this.pageHeight);
		}

		if (!dontUpdateBook) this.updateBook();
		this._insertingDoublePage = false;
	}, // insertDoublePage

	isDoublePage : function(content){
		content = $(content);
		return content.data("double") || content.is(this.opts.doublePages)
	}, // isDoublePage

	replaceNumberHolder : function(str, number){
		if (str==undefined) return str;
		number += "";
		return str.replace( /\{\{([^}]+)\}\}/g, function(match, p1){
			if (number.length < p1.length) {
				var zeroes = p1.replace(/./g, "0");
				return (zeroes + number).slice(-zeroes.length);
			}
			return number
		})
	}, // replaceNumberHolder

	loadPage : function(page){
		if (typeof(page)==='number') page=this.pages[page];
		if (!page || page.loaded || page.loading || !(page.src || page.image) ) return;
		page.loading = true;
		var book=this;
		if (page.src) {
			$.get(page.src, function(content){
				page.loaded = true;
				page.find('.wowbook-page-content').append(content);
				page.removeClass("wowbook-loading");
				book.updateThumbnail( page.pageIndex );
			})
		} else if (page.image) {
			var image = new Image();
			image.onload =  function(){
				page.loaded = true;
				page.find('.wowbook-page-content').append(this);
				$(this).addClass("wowbook-lazy");
				page.removeClass("wowbook-loading");
				book.updateThumbnail( page.pageIndex );
			};
			image.src = page.image;
		}
	}, // loadPage

	/*
	 * Remove pages
	 */
	removePages : function(from, to){
		if (!arguments.length) from=0, to=-1;
		if (this.holdedPage) this.releasePage(this.holdedPage);
		// based on Array Remove By John Resig (MIT Licensed)
		var pages = this.pages,
		    to = (to || from) + 1 || pages.length,
		    deleted = pages.slice(from, to),
		    rest  = pages.slice(to);
		pages.length = (from < 0) ? pages.length + from : from;
		pages.push.apply(pages, rest);
		for(var i=0,l=deleted.length;i<l;i++) {
			deleted[i].remove();
		}
		this.updateBook();
		return pages.length;
	}, // removePages


	/*
	 * updateBook
	 *
	 * update book after some page is inserted or removed.
	 */
	updateBook : function(dontShowPage){
		this.doPageNumbering();
		this.findPagesType();
		this.positionBookShadow();

		// apply left and right classes
		var onLeft = this.rtl, page;
		for(var i=0,l=this.pages.length;i<l;i++){
			page = this.pages[i].toggleClass('wowbook-left', onLeft).toggleClass('wowbook-right', !onLeft)
				.data({ pageIndex: i, holded: false });
			page.pageIndex = i;
			var content = $(".wowbook-page-content", page);
			page.src   = this.replaceNumberHolder( content.data("src") || this.opts.srcs, i);
			page.image = this.replaceNumberHolder( content.data("image") || this.opts.images, i);
			if (page.loaded!=true) page.loaded = (!page.src && !page.image);
			if (!page.loaded) page.addClass("wowbook-loading");
			page.onLeft = onLeft; page.onRight = !onLeft;
			onLeft = !onLeft;
		}
		this.findSections();
		if (!dontShowPage) this.showPage(this.currentPage);
	}, // updateBook

	/*
	 * Numerate the pages
	 */
	doPageNumbering : function(){
		var opts=this.opts;
		if (!opts.pageNumbers) return;
		var np = opts.numberedPages,
			lastPage = this.pages.length-1,
		    lastPageOnLeft = this.pageIsOnTheLeft(lastPage);

		if (np=="all") np = [0, -1];
		if (!np)       np = [2, lastPageOnLeft ? -3 : -2];

		var first = np[0],
		    last  = np[1];
		if (first<0) first=lastPage+first+1;
		if (first<0) first=0;
		if (first>this.pages.length-1) first=lastPage;
		if (last<0) last =lastPage+last+1;
		if (last<0) last=0;
		if (last>this.pages.length-1) last=lastPage;

		var content, pn, i,
		    pageNumber=this.opts.firstPageNumber;
		for (i=0; i<first; i++) $('.wowbook-page-number', this.pages[i]).remove();
		for (i=last+1; i<lastPage; i++) $('.wowbook-page-number', this.pages[i]).remove();
		for (i=first; i<=last; i++) {
			pn = $('.wowbook-page-number', this.pages[i]);
			if (!pn.length){
				content = $('.wowbook-page-content', this.pages[i]);
				pn = $('<div class="wowbook-page-number"></div>').appendTo(content);
			}
			pn.html(pageNumber++);
		}
	}, // doPageNumbering

	findPagesType : function(){
		var opts=this.opts,
			hp={}, index, i, l, isHardPage,
		    hardPages = opts.hardPages || [],
			allHardPages = (hardPages===true);

		if (!allHardPages) {
			// hard covers
			if (opts.hardcovers) {
				hardPages.push(0,1,-1);
				if (this.pageIsOnTheLeft(this.pages.length-1)) hardPages.push(-2);
			}

			// 'normalize' indexes and create a set
			for (i=0,l=hardPages.length;i<l;i++){
				index=hardPages[i];
				if (index<0) index=this.pages.length+index;
				if (index>=0 && index<this.pages.length) hp[index]=true;
			}
		}

		// force the second parameter to false when hp[i]===undefined, otherwise toggleClass will not remove the class
		i=this.pages.length;
		while(i--) {
			isHardPage = allHardPages || hp[i] || this.pages[i].hardPageSetByUser;
			this.pages[i].toggleClass('wowbook-hardpage', isHardPage).isHardPage = isHardPage;
		}
	}, // findPagesType

    showPage : function(pageIndex, updateLocationHash) {
		if (pageIndex < 0) pageIndex = 0;
		if (pageIndex > this.pages.length-1) pageIndex = this.pages.length-1;

		var leftpage  = this.leftPageIndex(pageIndex),
		    rightpage = this.rightPageIndex(pageIndex),
		    leftBelow  = this.pageBelow(leftpage),
		    rightBelow = this.pageBelow(rightpage),
		    width     = this.pageWidth,
		    onLeft    = this.rtl,
		    last      = this.pages.length-1,
		    zi, d;

		// lazy loading
		this.loadPage(leftpage);
		this.loadPage(rightpage);
		this.loadPage(leftBelow);
		this.loadPage(rightBelow);
		this.loadPage(this.backPage(leftpage));
		this.loadPage(this.backPage(rightpage));

		// set pages visibility/position
		for(var i=0, len=last; i<=len; i++) {
			zi = (this.pages[i].onLeft!=this.rtl) ? i : len-i;
			d = (i===leftBelow || i===leftpage || i===rightpage || i===rightBelow) ? 'block' : 'none';
			this.pages[i].data('zIndex', zi).css({
				display : d,
				left    : this.pages[i].onLeft ? 0 : width,
				top     : 0,
				zIndex  : zi
			});
			onLeft = !onLeft;
		} // s

		// enable/disable grab handles and nav controls
		var showingFirstPage = (pageIndex==0),
		    showingLastPage  = (pageIndex==last || pageIndex==this.otherPage(last));

		this.leftHandle.toggleClass('wowbook-disabled', !this.backPage(leftpage) );
		this.rightHandle.toggleClass('wowbook-disabled', !this.backPage(rightpage) );
		this.toggleControl("back",  showingFirstPage);
		this.toggleControl("next",  showingLastPage);
		this.toggleControl("first", showingFirstPage);
		this.toggleControl("last",  showingLastPage);

		// onShowPage callback
		var onShowPage = this.onShowPage;
		if (onShowPage && $.isFunction(onShowPage) && !this.isOnPage(pageIndex)) {
			this.currentPage = pageIndex;
			onShowPage(this, this.pages[pageIndex], pageIndex);
			var o=this.otherPage(pageIndex);
			if (o) onShowPage(this, this.pages[o], o);
		}

		this.currentPage = pageIndex;

		// centeredWhenClosed only 1 page visible
		if (this.centeredWhenClosed) {
			var lp = !!this.leftPage(pageIndex), rp=this.rightPage(pageIndex),
			    lefty = (lp && rp) ? 0 : (lp ? width/2 : -width/2 );
			this.origin.css('left', lefty );
		}

		this.positionBookShadow();

		if (updateLocationHash!==false
		 && this.opts.updateBrowserURL
		 && this.locationHashToPage()!=pageIndex) {
			this.locationHashSetTo = window.location.hash = this.pageToLocationHash(pageIndex);
		}

		this.showThumbnail()
	}, // showPage

	holdPage : function(page, x, y, corner, back) {
		if (typeof(page)==='number') page=this.pages[page];
		if (!page) return;
		var pageIndex = page.pageIndex,
		    last = this.pages.length-1,
		    lastPageIsAlone = !this.otherPage(last);

		if (!corner) corner=this.pageIsOnTheLeft(pageIndex) ? 'l' : 'r'
		else {
			if (!this.corners[corner] ||
			    (this.pageIsOnTheLeft(pageIndex) ? /r/ : /l/).test(corner) ) return;
		}

		if (back===undefined) back = this.backPage(pageIndex);
		if (!back) return;
		var backIndex = back.pageIndex;

		page.data('holded_info', [x,y,corner])

		if (this.centeredWhenClosed && (pageIndex===0 || backIndex===0 ||
				(lastPageIsAlone && (backIndex===last || pageIndex===last)))) {
			var lefty=0, newx, ltr = !this.rtl,
				width = this.pageWidth,
				trStart, trEnd,
				lrStart, lrEnd,
				xrStart, xrEnd, xbeforeStart, xafterEnd;
			if (ltr ? pageIndex===0 : (pageIndex===last && lastPageIsAlone)) {
				trStart = -width/2; trEnd = -width/4;
				lrStart = 0;        lrEnd = -width/2;
				xrStart = -width;   xrEnd = trEnd;
				xbeforeStart = xrStart; xafterEnd = x;
			}
			if (ltr ? (pageIndex===last && lastPageIsAlone) : pageIndex===0 ) {
				trStart = width;    trEnd = width*3/2;
				lrStart = width/2;  lrEnd = 0;
				xrStart = width;    xrEnd = width*2;
				xbeforeStart = x; xafterEnd = xrEnd;
			}
			if (ltr ? backIndex===0 : (backIndex===last && lastPageIsAlone)) {
				trStart = width/2;    trEnd = pageIndex===(ltr?last:0) ? width : width*3/2;
				lrStart = pageIndex===(ltr?last:0) ? width/2 : 0;        lrEnd = -width/2;
				xrStart = trStart;  xrEnd = width*2;
				xbeforeStart = x; xafterEnd = xrEnd;
			}
			if (ltr ? (backIndex===last && lastPageIsAlone) : backIndex===0)  {
				trStart = pageIndex===(ltr?0:last) ? 0 : -width/2; trEnd = width/2;
				lrStart =  width/2; lrEnd = pageIndex===(ltr?0:last) ? -width/2 : 0;
				xrStart = -width;   xrEnd = trEnd;
				xbeforeStart = xrStart; xafterEnd = x;
			}

			if (x<trStart) { lefty = lrStart; newx = xbeforeStart; }
			if (x>trEnd)   { lefty = lrEnd;   newx = xafterEnd;	}
			if (x>=trStart && x<=trEnd) {
				var px = (x-trStart)/(trEnd-trStart);
				lefty  = lrStart+px*(lrEnd-lrStart);
				newx   = xrStart+px*(xrEnd-xrStart);
			}
			x = newx;
			this.origin.css('left', lefty);
			this.positionBookShadow();
		}

		if (this.zoomed || this.pageType(page)=='basic' || this.pageType(back)=='basic' ) {
			this.foldPageBasic(page, x, y, corner, back);
		} else if (page.isHardPage || (back.isHardPage)) {
			this.holdHardpage(page, x, y, corner, back);
		} else {
			this.foldPage(page, x, y, corner, back);
		}

		if (!page.data('holded')) {
			page.addClass('wowbook-page-holded');
			back.addClass('wowbook-page-holded');
			page.data('holded', true);
			this.holdedPage = page;
			this.holdedPageBack = back;
			if (this.shadows) this.shadowClipper.css('display', 'block');
			if (this.clipBoundaries) this.clipper.css('overflow', 'visible');
			this.positionBookShadow();
			if (this.opts.onHoldPage) this.opts.onHoldPage(this, pageIndex, page, back);
		}
	}, // holdPage

	/*
	*	foldPage
	*/
	foldPage :function(page, x, y, corner, back){
		if (!this._currentFlip) this._currentFlip = this.foldPageStart(page, x, y, corner, back);
		if (this._currentFlip.page!=page) return

		this._currentFlip.x = x;
		this._currentFlip.y = y;
		this._currentFlip.page.data('holdedAt', {x: x, y: y });
		this._currentFlip.corner = corner;
		this.foldPageStyles(this._currentFlip);
	}, // foldPage

	foldPageStart: function(page, x, y, corner, back){
		var flip = {};

		if (typeof(page)==='number') page=this.pages[page];
		flip.book = this;
		flip.page = page;
		flip.pageIndex = page.data('pageIndex');

		if (back===undefined) back = this.backPage(flip.pageIndex);
		if (!back || !back.length) return;
		flip.back = back;

		// contents
		flip.pageContent = page.children().first();
		flip.backContent = back.children().first();

		// helpers
		var width      = this.pageWidth,
		    height     = this.pageHeight,
		    halfWidth  = width/2,
		    halfHeight = height/2;

		// corner
		if (!corner) corner='tl';
		if (corner=='l' || corner=='r') {
			var grabPoint = {
				x: (corner=='l') ? 0 : width,
				y: y
			};
			page.data('grabPoint', grabPoint);
			flip.grabPoint = grabPoint;
			corner = ( (y>=grabPoint.y) ? 't' : 'b') + corner;








		}

		flip.page.data('holdedAt', {x: x, y: y });
		flip.x = x;
		flip.y = y;
		flip.page.data('holdedCorner', corner);
		flip.corner = corner;
		flip.pageDiagonal = Math.sqrt(width*width+height*height);

		// inicializacao
		flip.page.css("clip", 'rect(-1000px 2000px 2000px 0px)');

		flip.pageLeft = parseFloat(page.css('left'));
		back.css({
			left   : flip.pageLeft+"px",
			zIndex : 1000,
			clip   : 'rect(-1000px 2000px 2000px 0px)'
		});
		// shadow
		flip.shadowHeight = 2*Math.ceil( flip.pageDiagonal ),
		flip.shadowTop    = -(flip.shadowHeight-height)/2;
		this.internalShadow.css({
			display : 'block',
			height : flip.shadowHeight
		});
		flip.foldShadowWidth = this.foldShadow.width();
		this.foldShadow.css({
			display: 'block',
			height : flip.shadowHeight
		});

		// foldGradient
		this.foldGradientContainer.appendTo(flip.backContent);
		flip.foldGradientWidth  = this.foldGradientElem.width();
		flip.foldGradientHeight = 2*Math.ceil( flip.pageDiagonal );
		this.foldGradientElem.css('height', flip.foldGradientHeight)
		this.foldGradientContainer.css({
			position : 'absolute',
			width    : flip.foldGradientWidth,
			height   : flip.foldGradientHeight,
			top      : 0,
			left     : 0,
			display  : "none"
		})
		flip.foldGradientVisible = false;

		return flip
	}, // foldPageStart

	foldPageStyles : function(flip){
		var width      = this.pageWidth,
		    height     = this.pageHeight,
		    halfWidth  = width/2,
		    halfHeight = height/2,
		    translate  = $.wowBook.utils.translate;

		var pageLeft = flip.pageLeft,
		    x=flip.x, y=flip.y, back=flip.back;

		// corner
		var corner = flip.corner || "tl";
		if (corner=='l' || corner=='r') {
			var grabPoint=flip.page.data('grabPoint');
			if (!grabPoint) {
				grabPoint = {
					x: (corner=='l') ? 0 : width,
					y: y
				};
				page.data('grabPoint', grabPoint);
			};
			corner = ( (y>=grabPoint.y) ? 't' : 'b') + corner;
			corner = ( (y>=grabPoint.y) ? 't' : 'b') + (this.pageIsOnTheLeft(flip.pageIndex) ? "l" : "r");
			flip.corner = corner;
			flip.page.data('holdedCorner', corner);

			var dx    = (x-grabPoint.x),
			    dy    = (y-grabPoint.y),
			    angle = Math.atan2(dy,dx),
			    corn  = { x: 0, y: (y>=grabPoint.y) ? 0 : height },
			    n     = { x: 0,	y: corn.y-grabPoint.y };
			n = rotatePoint(n, 2*angle)
			x = n.x+x;
			y = n.y+y;
		}

		flip.page.data('holdedAt', {x: x, y: y });
		flip.page.data('holdedCorner', corner);

		// first fixed corner
		var cornerxy = this.corners[corner],
		    fx = width-cornerxy[0],
		    fy = cornerxy[1];
		var dx = (x-fx),
		    dy = (y-fy),
		    distance = Math.sqrt(dx*dx+dy*dy);
		if (distance > width) {
			x = fx+(width*dx/distance);
			y = fy+(width*dy/distance);
		}

		// second fixed corner
		fy = height-fy;
		var dx = (x-fx),
		    dy = (y-fy),
		    distance = Math.sqrt(dx*dx+dy*dy),
		    maxdistance = flip.pageDiagonal ;
		if (distance > maxdistance) {
			x = fx+(maxdistance*dx/distance);
			y = fy+(maxdistance*dy/distance);
		}

		var cx = cornerxy[0], cy=cornerxy[1];

		if (cy==y) y=cy+0.001;

		var dx = (x-cx),
		    dy = (y-cy),
		    distance = Math.sqrt(dx*dx+dy*dy),
		    halfd    = distance/2,
		    angle    = Math.atan2(dy,dx),
		    tan_a    = Math.tan(angle),
		    ar       = angle,
		    angle    = angle*180/Math.PI;



		var	bc  = { x : cx-halfWidth, y: halfHeight-cy },
			bc2 = rotatePoint(bc, ar);
		var xcut = bc2.x+halfd + halfWidth + 0.5;

		flip.pageContent.css('transform', translate(-xcut, 0)+' rotate('+(-angle).toFixed(7)+'deg)');
		flip.page.css('transform', translate((Math.cos(ar)*xcut).toFixed(5), (Math.sin(ar)*xcut).toFixed(5))+' rotate('+angle.toFixed(7)+'deg)' );

		/* shadow */
		var op = this.calculateOpacity(halfd, width, this.shadowThreshold, 50);
		if (this.shadows && (op > 0)) {
			var left = xcut+pageLeft,
			    top  = flip.shadowTop;
			this.internalShadow.css({
				transform: translate(left, top)+' rotate('+angle+'deg)',
				transformOrigin : halfWidth-xcut+"px "+(halfHeight+(flip.shadowHeight-height)/2)+"px"
			});

			var ls = xcut-flip.foldShadowWidth;

			this.foldShadow.css({
				transform: translate(ls+pageLeft, top)+' rotate('+angle+'deg)',
				transformOrigin : halfWidth-ls+"px "+(halfHeight+(flip.shadowHeight-height)/2)+"px"
			});

			this.shadowContainer.css({ opacity : op, display : 'block' });
		} else {
			this.shadowContainer.css("display", "none");
		}

		// back
		back.show();


		bc.x = -bc.x;
		var bc2  = rotatePoint(bc, -ar);
		var xcut = bc2.x-halfd + halfWidth - 1;

		var t1, t2;
		t1 = { x : bc2.x-halfd, y : bc2.y+halfd*tan_a }
		t2 = { x : bc2.x-halfd, y : bc2.y-halfd/(tan_a==0 ? 0.0001 : tan_a) }
		t1 = rotatePoint(t1, -ar);
		t2 = rotatePoint(t2, -ar);
		t2 = -(t2.x + halfWidth);
		t1 = -(t1.y - halfHeight);

		flip.backContent.css('transform', translate(-xcut, 0)+' rotate('+angle+'deg)' );
		flip.back.css('transform', translate((cx+t2+Math.cos(ar)*xcut).toFixed(5), (cy-t1+Math.sin(ar)*xcut).toFixed(5))+' rotate('+angle+'deg)');



		// fold Gradient
		var op = this.calculateOpacity(halfd*2, width*2, this.foldGradientThreshold, 50);
		if (this.foldGradient && (op > 0)) {

			this.foldGradientContainer.css({
				opacity   : op,
				display   : 'block',
				transform : translate(((width-cx)-flip.foldGradientWidth/2), (cy-flip.foldGradientHeight/2))+' rotate('+(-angle)+'deg)'
			});
			this.foldGradientElem.css("transform", translate(-halfd+flip.foldGradientWidth/2, 0));

			if (!flip.foldGradientVisible) {
				this.foldGradientContainer.css("display", "block");
				flip.foldGradientVisible = true;
			}

		} else {
			if (flip.foldGradientVisible) {
				this.foldGradientContainer.css("display", "none");
				flip.foldGradientVisible = false;
			}
		}
	}, // foldPageStyles




	holdHardpage : function(page, x, y, corner, back) {
		if (!this._currentFlip) this._currentFlip = this.flipHardPageStart(page, x, y, corner, back);
		if (this._currentFlip.page!=page) return

		this._currentFlip.x = x;
		this._currentFlip.y = y;
		this._currentFlip.page.data('holdedAt', {x: x, y: y });
		this._currentFlip.corner = corner;

		this.flipHardPageStyles(this._currentFlip);
	}, // holdHardpage

	flipHardPageStart : function(page, x, y, corner, back) {
		if (this.clipBoundaries) this.clipper.children('.wowbook-inner-clipper').css('overflow', 'visible');

		var flip = {};

		if (typeof(page)==='number') page=this.pages[page];
		flip.book = this;
		flip.page = page;
		flip.pageIndex = page.data('pageIndex');

		if (back===undefined) back = this.backPage(flip.pageIndex);
		if (!back || !back.length) return;
		flip.back = back;

		// helpers
		var width      = this.pageWidth,
		    height     = this.pageHeight,
		    halfWidth  = width/2,
		    halfHeight = height/2;

		if (!corner) corner='tl';
		page.data('holdedAt', {x: x, y: y });
		page.data('holdedCorner', corner);

		page.css("zIndex", 1000);
		back.css("zIndex", 1000);

		if (this.opts.use3d && Modernizr.csstransforms3d) {
			page.css(Modernizr.prefixed('perspectiveOrigin'), '0 50%');
			back.css(Modernizr.prefixed('perspectiveOrigin'), '0 50%');
		}
		var x0 = (this.pageIsOnTheLeft(flip.pageIndex) ? width : 0);
		page.css("transformOrigin", x0+'px 50%');
		back.css("transformOrigin", (width-x0)+'px 50%');

		// shadow
		if (this.shadows) this.hardPageShadow.css('display', 'block');

		return flip
	}, // flipHardPageStart

	flipHardPageStyles : function(flip) {
		var page       = flip.page,
		    back       = flip.back;
	        x=flip.x, y=flip.y;

		var onRight   = this.pageIsOnTheRight(flip.pageIndex),
		    width     = this.pageWidth,
		    height    = this.pageHeight,
		    corner    = flip.corner;

		if (!corner) corner='tl';
		page.data('holdedAt', {x: x, y: y });
		page.data('holdedCorner', corner);

		var dx    = onRight ? width-x : x,
		    fixed = onRight ? 0       : width,
		    p, same;
		if (dx<0) dx=0;
		same = dx < width;
		p = same ? page : back;
		(same ? back : page).css('display', 'none');
		var pIsOnLeft = onRight!=same,
		    cx        = x-fixed;
		if (cx>width)  cx=width;
		if (cx<-width) cx=-width;
		var cy     = -Math.sqrt( 40*40*(1-cx*cx/((width+15)*(width+15))) ),
		    scaleX = Math.abs(cx/width),
		    angle  = scaleX==1 ? 0 : Math.atan2(cy,cx);

		if (this.opts.use3d && Modernizr.csstransforms3d) {


			var roty;
			if (pIsOnLeft)
				roty = -this._calculateAngleFromX(-cx, width)
			else
				roty = this._calculateAngleFromX(cx, width)

			if (this.animating){
				var anim = this._animationData;
				if (this.curledPage || anim.curled ) {
					anim.curled = true
					if (!anim.angle){
						var angle = { from : roty, to : 0 }
						anim.angle = angle;
						var cx2 = cx+anim.dx;
						if (pIsOnLeft)
							angle.to = -this._calculateAngleFromX(-cx2, width)
						else
							angle.to = this._calculateAngleFromX(cx2, width)
						if (Math.abs(cx)==width) angle.from = 0
						if (Math.abs(cx2)==width) angle.to = 0
						angle.delta = angle.to-angle.from
					}
					roty = anim.angle.from - anim.angle.delta*(anim.from.x-x)/anim.dx
				} else if ( Math.abs(x-anim.from.x)>Math.abs(anim.dx/2) ) {






				}
			}

			p.css({
				transform : 'perspective('+this.opts.perspective+this.perspectiveUnit+') rotate3d(0, 1, 0, '+(roty)+'deg)',
				display   : 'block'
			});
		} else {
			p.css({
				transform : 'skewY('+angle+'rad) scaleX('+scaleX+')',
				display   : 'block'
			});
		}

		if (!$.wowBook.support.transform && $.wowBook.support.filters) {
			var matrix = "M11="+scaleX+", M12=0, M21="+Math.tan(angle)*scaleX+", M22=1";
			// for some reason putting margins with filter in the same $().css call doesn't work
			p.css('filter', "progid:DXImageTransform.Microsoft.Matrix("+matrix+", sizingMethod='auto expand')" );
			p.css({
				marginTop  : height-p.height(),
				marginLeft : ( pIsOnLeft ? width-p.width() : 0)
			});
		}

		// shadow
		if (this.shadows) this.hardPageShadow.css({
			left    : pIsOnLeft ? 0 : width,
			opacity : Math.abs(cx/width)*0.5
		});
	}, // flipHardPageStyles


	_calculateAngleFromX : function(x, width, perspective){
		var halfWidth = width*2/3;
		if ( x>halfWidth ) {
			var startAngle = this._calculateAngleFromX(halfWidth, width, perspective),
			    endAngle   = 0,
			    dx         = (x-halfWidth)/(width-halfWidth),
			    angle      = startAngle+(endAngle-startAngle)*dx;
			return angle
		}
		perspective = perspective || this.opts.perspective
		var angle, rad2deg = 180/Math.PI,
		    w2      = width*width, p2= perspective*perspective, x2= x*x;
		angle = Math.acos( (width*p2*x - Math.sqrt(w2*w2*p2*x2 + w2*w2*x2*x2-w2*p2*x2*x2))/(w2*p2 + w2*x2));
		angle = -angle * rad2deg;
		return angle;
	}, // _calculateAngleFromX


	// foldPageBasic, does not use CSS transform
	foldPageBasic : function(page, x, y, corner, back) {
		if (!this._currentFlip) this._currentFlip = this.foldPageBasicStart(page, x, y, corner, back);
		if (!this._currentFlip || this._currentFlip.page!=page) return

		this._currentFlip.x = x;
		this._currentFlip.y = y;
		this._currentFlip.page.data('holdedAt', {x: x, y: y });
		this._currentFlip.corner = corner;
		this.foldPageBasicStyles(this._currentFlip);
	}, // foldPageBasic

	foldPageBasicStart : function(page, x, y, corner, back) {
		var flip = {};

		if (typeof(page)==='number') page=this.pages[page];
		flip.book = this;
		flip.page = page;
		flip.pageIndex = page.data('pageIndex');

		if (back===undefined) back = this.backPage(flip.pageIndex);
		if (!back || !back.length) return;
		flip.back = back;

		// helpers
		var width      = this.pageWidth,
		    height     = this.pageHeight;

		if (!corner) corner='tl';
		page.data('holdedAt', {x: x, y: y });
		page.data('holdedCorner', corner);

		back.css('zIndex', 1000);
		page.data('foldPageBasic', true);
		flip.foldGradientWidth  = this.foldGradientElem.width();
		flip.foldShadowWidth = this.foldShadow.width();
		this.internalShadow.css('display', 'none');
		this.foldShadow.css({
			display   : 'none',
			height    : height,
			transform : '',
			top       : 0
		}).toggleClass('wowbook-shadow-fold-flipped', page.onRight);
		this.shadowContainer.css('display', 'block');
		var backContent = back.children().first();
		this.foldGradientContainer
			.appendTo(backContent)
			.css({ width : flip.foldGradientWidth,  height : height, top : 0, transform: '', zIndex: 1000000000 });
		this.foldGradientElem.css({
			left   : 0,
			height : height
		}).toggleClass('wowbook-fold-gradient-flipped', page.onRight);

		return flip
	}, // foldPageBasicStart

	foldPageBasicStyles : function(flip) {
		var page   = flip.page,
		    back   = flip.back;
		    x=flip.x, y=flip.y;

		var width  = this.pageWidth,
		    height = this.pageHeight,
		    corner = flip.corner;

		if (!corner) corner='tl';
		page.data('holdedAt', {x: x, y: y });
		page.data('holdedCorner', corner);

		var onLeft = this.pageIsOnTheLeft(flip.pageIndex),
		    fixed  = onLeft ? width : 0 ,
		    dx     = onLeft ?     x : width-x;
		if (dx<0) dx=0;
		if (dx>2*width) dx=2*width;
		var halfd = dx/2;
		var pageclip, backclip, leftb;
		if (onLeft) {
			pageclip = 'rect(-1000px 1000px 1000px '+halfd+'px)';
			backclip = 'rect(-1000px 1000px 1000px '+(width-halfd)+'px)';
			leftb    = dx-width;
		} else {
			pageclip = 'rect(-1000px '+(width-halfd)+'px 1000px -1000px)';
			backclip = 'rect(-1000px '+halfd+'px 1000px -1000px)';
			leftb    = width-dx+width;
		}

		page.css('clip', pageclip);



		back.css({ clip: backclip, left: leftb, display:'block' });

		// shadow
		var op = this.calculateOpacity(halfd*2, width*2, this.shadowThreshold, 50);
		if (this.shadows && (op > 0)) {
			var leftx = onLeft ?  halfd-flip.foldShadowWidth : width-halfd + width;
			this.shadowContainer.css('opacity', op);
			this.foldShadow.css({
				left    : leftx,
				display : 'block'
			});
		} else {
			this.foldShadow.css('display', 'none');
		}

		// Gradient
		var op = this.calculateOpacity(halfd*2, width*2, this.foldGradientThreshold, 50);
		if (this.foldGradient && (op > 0)) {
			var leftx = onLeft ? width-halfd : halfd-flip.foldGradientWidth;
			this.foldGradientContainer.css({
				opacity  : op,
				left     : leftx,
				display  : 'block'
			});
		} else {
			this.foldGradientContainer.css('display', 'none');
		}
	}, // foldPageBasicStyles


	animateFoldPage : function(page, corner, from, to, callback, arc, back, duration) {
		var book = this;
		if (book.animating) return;
		book.animating = true;
		if (!from) from = page.data('holdedAt');
		if (!corner) corner = page.data('holdedCorner');

		var dx = (from.x-to.x),
		    dy = (from.y-to.y),
		    x, y;
		if (duration==undefined) duration = this.turnPageDuration * Math.abs(dx)/(this.pageWidth*2);
		if (duration<this.opts.turnPageDurationMin) duration=this.opts.turnPageDurationMin

		if (!page.isHardPage && duration/this.turnPageDuration>0.4) this.playFlipSound();

		this._animationData = {from: from, to: to, dx: -dx}
		this.holdPage(page, from.x, from.y, corner, back);
		this._percent = 0;
		$(this).animate({_percent:1}, {
			duration : duration,
			easing   : 'linear',
			complete : function(){
				book.animating = false;
				if ($.isFunction(callback)) callback();
			},
			step:function(e, b){
				x = from.x-e*dx;
				y = from.y-e*dy;
				if (arc) y -= (0.5-Math.abs(0.5-e))*book.pageHeight/10;
				book.holdPage(page, x, y, corner, back);
			}
		})

	}, // animateFoldPage

	stopAnimation : function(jumpToEnd){
		if (!arguments.length) jumpToEnd=true
		$(this).stop(true, jumpToEnd);
		this.animating = false;
	}, // stopAnimation

	// valid options:
	//		from: [x,y] initial x,y coordinates
	//		to: [x,y] final x,y coordinates
	//		page:
	//		back:
	//		corner :
	//		duration:
	//		easing: easing function
	//		complete : callback function called once the animation is complete.
	flip : function(x, y, page, options) {
		if (!options) options = ($.isPlainObject(x) ? x : {});
		if (!options.from) options.from=[]
		if (!options.to) options.to=[]
		var book = this;

		if (book.animating) return
		book.animating = true;

		var flipCompleted = function(){
			book.animating = false;
			if ($.isFunction(options.complete)) options.complete();
		}
		if (!page) page = options.page || book.holdedPage;
		var hi = page.data('holded_info');
		var initial = page.data('holdedAt') || {};
		var corner  = options.corner || page.data('holdedCorner');
		var easing  = $.easing[options.easing] || options.easing

		              || function(x){ return (x==1) ? 1 : (-Math.pow(2, -10 * x) + 1) };
		var flip = {
			page     : page,
			back     : options.back || book.holdedPageBack || book.backPage(page.pageIndex),




			initialX : options.from[0]!=undefined ? options.from[0] : hi[0],
			initialY : options.from[1]!=undefined ? options.from[1] : hi[1],
			finalX   : options.to[0]!=undefined ? options.to[0] : x,
			finalY   : options.to[1]!=undefined ? options.to[1] : y,
			corner   : corner || hi[2],
			duration : options.duration,
			complete : flipCompleted,
			easing   : easing,
			arc      : options.arc,
			dragging : options.dragging,
			start    : $.now(),
			finished : false
		}
		flip.deltaX = flip.finalX - flip.initialX;
		flip.deltaY = flip.finalY - flip.initialY;



		this._animationData = {
			from: {x: flip.initialX, y: flip.initialY},
			to: {x: flip.finalX, y: flip.finalY},
			dx: flip.deltaX
		}

		if (flip.duration==undefined) flip.duration = this.turnPageDuration * Math.abs(flip.deltaX)/(this.pageWidth*2);
		if (flip.duration<this.opts.turnPageDurationMin) flip.duration=this.opts.turnPageDurationMin
		if (!page.isHardPage && flip.duration/this.turnPageDuration>0.4) this.playFlipSound();


		this.currentFlip = flip;
	}, // flip

	rafCallback: function(){
		window.raf(this.callRAFCallback);
		this._zoomUpdateOnRAF();

		if (!this.currentFlip || this.currentFlip.finished) return;

		var flip    = this.currentFlip,
		    percent = ( $.now()-flip.start )/flip.duration;
		if (percent>=1) percent=1;


		flip.x = flip.initialX+flip.deltaX*flip.easing(percent, flip.duration*percent, 0, 1, flip.duration);
		flip.y = flip.initialY+flip.deltaY*flip.easing(percent, flip.duration*percent, 0, 1, flip.duration);
		if (flip.arc) flip.y -= (0.5-Math.abs(0.5-flip.easing(percent, flip.duration*percent, 0, 1)))*this.pageHeight/10;
		if (flip.dragging){
			flip.x = flip.initialX+flip.deltaX*0.2;
			flip.y = flip.initialY+flip.deltaY*0.2;
			flip.initialX = flip.x; flip.initialY = flip.y;
			flip.deltaX = flip.finalX - flip.initialX;
			flip.deltaY = flip.finalY - flip.initialY;
			if (flip.deltaX<1 && flip.deltaY<1) percent==1;
		}
		this.holdPage(flip.page, flip.x, flip.y, flip.corner, flip.back);
		if (percent==1) {
			flip.finished=true;
			if (flip.complete) flip.complete();
		}
	}, // rafCallback


	releasePages : function(){
		for (var i=0,l=this.pages.length;i<l;i++){
			if (this.pages[i].data('holded')) this.releasePage(i);
		}
	}, // releasePages



	releasePage : function(page, animated, back, duration){
		if (typeof(page)==='number') page=this.pages[page];
		var book=this,
			from   = page.data('holdedAt'),
			corner = page.data('holdedCorner');
		if (animated && from) {





			this.flip({ from: [from.x, from.y], to: this.corners[corner], page: page,
				easing   : 'linear',
				duration : 10000, //duration,
				duration : duration,
				complete : function(){ book.releasePage(page); }
			})
			return
		}
		var pageIndex = page.data('pageIndex');

		if (back===undefined) back = this.holdedPageBack || this.backPage(pageIndex);
		this.holdedPage = null;
		this.holdedPageBack = null;
		page.data({
			holded_info   : null,
			holdedAt      : null,
			holdedCorner  : null,
		    grabPoint     : false,
			foldPageBasic : null,
			holded        : false
		});
		if (this.clipBoundaries && !this.zoomed) {
			this.clipper.css('overflow', 'hidden');
			this.clipper.children('.wowbook-inner-clipper').css('overflow', 'hidden');
		}

		this.shadowClipper.css('display', 'none');

		this.internalShadow.parent().hide();
		this.foldGradientContainer.hide();
		this.hardPageShadow.hide();
		this.resetPage(page);

		if (back && back.length) {
			this.resetPage(back);
			back.hide();
		}

		this.foldShadow.removeClass('wowbook-shadow-fold-flipped')
			.css({ transform: '', left: '' });
		this.foldGradientElem.removeClass('wowbook-fold-gradient-flipped')
			.css('transform', '');
		this.foldGradientContainer.css('transform', '').appendTo(this.pagesContainer);
		this.positionBookShadow();
		if (this.opts.onReleasePage) this.opts.onReleasePage(this, pageIndex, page, back);
	}, // releasePage

	resetPage : function(page){
		this._currentFlip = undefined;
		page.removeClass('wowbook-page-holded');
		if (!this.resetCSS) this.resetCSS = {
			transform           : '',
			transformOrigin     : '',
			clip                : 'auto',
			marginLeft          : 0,
			marginTop           : 0,
			filter              : ''
		};
		var w=this.pageWidth, h=this.pageHeight;
		page.css(this.resetCSS)
		  .css({ zIndex: page.data('zIndex'), width: w, height: h
			  ,left: this.pageIsOnTheLeft(page.data('pageIndex')) ? 0 : w
		  });
		// what can i say? IE SUCKS
		if ($.browser.msie && $.browser.version<9)
			page.attr('style', page.attr('style').replace(/clip\: [^;]+;/i, ''));

		var content = $('.wowbook-page-content', page);
		content.css(this.resetCSS);
		boxSizingBorderBox(content, w, h);
	}, // resetPage

	gotoPage : function(pageIndex, updateBrowserURL){
		if (this.animating) return;
		this._cantStopAnimation = true;
		if ((typeof pageIndex==='string') && pageIndex.charAt(0)=='#') pageIndex=this.selectorToPage(pageIndex);
		if (pageIndex<0) pageIndex = 0;
		if (pageIndex>this.pages.length-1) pageIndex = this.pages.length-1;
		if (this.isOnPage(pageIndex)) return;

		var goingBack = (pageIndex < this.currentPage),
		    goingLeft = (this.rtl ? (pageIndex > this.currentPage) : goingBack);

		var book = this,
		    page = goingLeft ? book.leftPage() : book.rightPage();
		if (!page) return;

		this.uncurl(true)

		var pageBelow, back;
		if (goingLeft) {
			pageBelow = this.leftPage(pageIndex);
			back      = this.rightPage(pageIndex);
		} else {
			pageBelow = this.rightPage(pageIndex);
			back      = this.leftPage(pageIndex);
		}

		var backIsVisible = back && back.is(":visible");

		// put the page to be shown below the current page
		if (goingBack) {
			for(var i=page.pageIndex-1; i>=0; i--)
				this.pages[i].css('display', 'none');
		} else {
			for(var i=page.pageIndex+1, len=this.pages.length; i<len; i++)
				this.pages[i].css('display', 'none');
		}
		if (pageBelow) pageBelow.css('display', 'block');
		// without this, back page might blink
		if (backIsVisible) back.css('display', 'block');

		var pn = pageIndex;

		// turns the page
		var isHolded = page.data('holdedAt'),
			from     = page.data('holdedAt'),
			to,
		    corner   = page.data('holdedCorner') || (goingLeft ? 'tl' : 'tr');

		if (goingLeft) {
			from = from || { x:0, y:0};
			to   = {
				x: book.pageWidth*2,
				y: (corner!='bl' ? 0 : this.pageHeight)
			};
		} else {
			from = from || { x:this.pageWidth, y:0},
			to   = {
				x: -book.pageWidth,
				y: (corner!='br' ? 0 : this.pageHeight)
			};
		}






		var easing='linear';
		if (this.centeredWhenClosed && (page.isHardPage || back.isHardPage)) {
			var lastPage = this.pages.length-1,
			    ltr = !this.rtl;
			easing = 'easeOutCubic'
			if (this.currentPage==(ltr ? 0 : lastPage)) {
				to.x += this.pageWidth/2;
				if (ltr ? ((pageIndex==lastPage) && this.pageIsOnTheLeft(pageIndex)) : (pageIndex==0)) {
					to.x += this.pageWidth/2;
				}
			}
			if (this.currentPage==(ltr ? lastPage : 0)) {
				to.x -= this.pageWidth/2;
				if (pageIndex==(ltr ? 0 : lastPage)) {
					to.x -= this.pageWidth/2;
				}
			}
		}

		book.flip({
			from     : [from.x, from.y],
			to       : [to.x, to.y],
			easing   : easing,
			arc      : !isHolded,
			page     : page,
			back     : back,
			corner   : corner,
			complete : function(){
				book._cantStopAnimation = false;
				book.releasePage(page, false);
				book.showPage(pn, updateBrowserURL);
			}
		});

		return pageIndex;
	}, // gotoPage

	back : function(){
		return this.gotoPage(this.currentPage-2);
	}, // back

	advance : function(){
		return this.gotoPage(this.currentPage+2);
	}, // advance

	leftPage : function(pageIndex){
		if (pageIndex===undefined) pageIndex = this.currentPage;
		return this.pages[ this.leftPageIndex(pageIndex) ] || null;
	}, // leftPage

	leftPageIndex : function(pageIndex){
		if (!this.pageIsOnTheLeft(pageIndex)) pageIndex += (this.rtl ? 1 : -1);
		if (pageIndex<0 || pageIndex>this.pages.length-1) pageIndex=null;
		return pageIndex;
	}, // leftPageIndex

	rightPage : function(pageIndex){
		if (pageIndex===undefined) pageIndex = this.currentPage;
		return this.pages[ this.rightPageIndex(pageIndex) ] || null;
	}, // rightPage

	rightPageIndex : function(pageIndex){
		if (!this.pageIsOnTheRight(pageIndex)) pageIndex += (this.rtl ? -1 : 1);
		if (pageIndex<0 || pageIndex>this.pages.length-1) pageIndex=null;
		return pageIndex;
	}, // rightPageIndex

	pageIsOnTheRight : function(pageIndex) {
		return this.rtl ? !!(pageIndex%2) : !(pageIndex%2);
	}, // pageIsOnTheRight

	pageIsOnTheLeft : function(pageIndex) {
		return this.rtl ? !(pageIndex%2) : !!(pageIndex%2);
	}, // pageIsOnTheLeft

	otherPage : function(pageIndex) {
		if (this.pageIsOnTheLeft(pageIndex)) { pageIndex += (this.rtl ? -1 : 1); }
		else { pageIndex += (this.rtl ? 1 : -1); }
		if (pageIndex<0 || pageIndex>this.pages.length-1) pageIndex=null;
		return pageIndex;
	}, // otherPage

	isOnPage:function(pageIndex) {
		return (typeof pageIndex==='number') &&
		       (pageIndex===this.currentPage || pageIndex===this.otherPage(this.currentPage));
	}, // isOnPage

	backPage: function(pageIndex) {
		if (!this.pages[pageIndex]) return null;
		pageIndex += (pageIndex%2 ? -1 : 1);
		return this.pages[pageIndex];
	}, // backPage

	pageBelow: function(pageIndex) {
		pageIndex = parseInt(pageIndex, 10);
		if ( pageIndex!=pageIndex ) return null // if pageIndex is NaN



		var below = pageIndex + ( this.pageIsOnTheLeft(pageIndex)!=this.rtl ? -2 : 2);
		if (below<0 || below>this.pages.length-1) below=null;
		return below;
	}, // pageBelow

	pageType: function(pageIndex){
		var page;
		page = (typeof pageIndex==='number') ? this.pages[pageIndex] : pageIndex;
		return page.isHardPage ? "hard" :
		       page.find('.wowbook-page-content.wowbook-basic-page').length ? "basic" : "soft";
	},

	calculateOpacity : function(value, max, thresholdMin, thresholdMax) {
		if (value<=thresholdMin || value>=(max-thresholdMin) )  return 0;
		if (value>=thresholdMax && value<=(max-thresholdMax) )  return 1;
		var d=thresholdMax-thresholdMin;
		if (value > thresholdMax) value = max-value; // upper bands
		return (value-thresholdMin)/d;
	}, // calculateOpacity

	//
	//
	// Slideshow methods
	//
	//
	startSlideShow : function(){
		this.slideShowRunning = true;
		this.advanceAfterTimeout(this.slideShowDelay);
		$(this.opts.controls.slideShow).addClass('wowbook-disabled');
	}, // startSlideShow

	advanceAfterTimeout : function(delay){
		var book=this;
		this.slideShowTimer = setTimeout(function(){
			if (book.animating || book.holdedPage) { book.advanceAfterTimeout(100); return };
			book.advance();
			if (!book.isOnPage(book.pages.length-1))
				book.advanceAfterTimeout(book.slideShowDelay+book.turnPageDuration)
			else
				book.stopSlideShow();
		}, delay);
	}, // advanceAfterTimeout

	stopSlideShow : function(){
		clearTimeout( this.slideShowTimer );
		this.slideShowTimer = undefined;
		this.slideShowRunning = false;
		$(this.opts.controls.slideShow).removeClass('wowbook-disabled');
	}, // stopSlideShow

	//
	// toggleSlideShow
	//
	toggleSlideShow : function(){
		this.slideShowRunning ? this.stopSlideShow() : this.startSlideShow()
	}, // toggleSlideShow


	//
	//
	// Sections
	//
	//
	findSections : function(s){
		if (s) this.sectionDefinition = s;
		var sectionDef = this.sectionDefinition,
			sections = [],
		    section;

		if (typeof(sectionDef)==='string') {
			section  = sectionDef;
			sectionDef = [];
			$(section, this.elem).each(function(i,e){
				sectionDef.push([ '#'+e.id, $(e).html() ]);
			});
		}
		if ($.isArray(sectionDef)) {
			for(var i=0, l=sectionDef.length; i<l; i++) {
				section = sectionDef[i];
				if (typeof(section)==='string') {
					try { section = [section, $(section, this.elem).html()]; }
					catch(e) {
						//this.log("Something wrong happened at the function 'findSections' (maybe you have passed a invalid jquery selector?) :<br/>&nbsp;&nbsp;"+e)
						continue;
					}
				}
				try { section[2] = this.selectorToPage(section[0]); }
				catch(e){
						//this.log("Something wrong happened at the function 'findSections' (maybe you have passed a invalid jquery selector?) :<br/>&nbsp;&nbsp;"+e)
						continue;
				}
				if (section[2]===undefined) continue;
				sections.push({ id: section[0], title: section[1], page: section[2] });
			}
			sections = sections.sort(function(a,b){ return a.page-b.page });
		}
		this.sections = sections;
		return sections;
	}, // findSections


	/*
	 * method pageToSection
	 *
	 * returns the section that the given page belongs
	 *
	 * params
	 * 		pageIndex : index of the page
	 *
	 * returns
	 * 		an object containing the section info.
	 */
	pageToSection : function(pageIndex){
		var sections = this.sections,
			section;
		for(var i=0,l=sections.length; i<l; i++){
			if (sections[i].page > pageIndex) break;
			section=sections[i];
		}
		return section;
	},

	/*
	 * method currentSection
	 *
	 * returns the section that is being showed in the book
	 *
	 */
	currentSection : function(){
		return this.pageToSection(this.currentPage);
	}, // currentSection

	//
	// TOC
	//
	// Experimental, use at your own risk!
	//
	fillToc : function(element, template){
		var toc = $(element || this.opts.toc),
		    sections, section, item,
		    wrapper = '';
		if (toc.length===0) return;

		sections = this.sections;
		if (typeof(template)==='undefined') template = this.opts.tocTemplate;

		if (!template) {
			wrapper  = (toc.is('UL, OL')) ? '<li>' : '<div>';
			template = '<a href="${link}">${section}</a>';
		}

		for(var i=0, l=sections.length; i<l; i++) {
			section = sections[i];
			item = template.replace(/\$\{link\}/g, '#'+this.id+'/'+section.id.substr(1))
				.replace(/\$\{section\}/g, section.title )
				.replace(/\$\{page\}/g, section.page );
			$(item).appendTo(toc).wrap(wrapper);
		}
	}, // fillToc



	// Converts a windows.location.hash into a page index
	// that matches that hash
	// #bookid/numberX    => page index X
	// #bookid/elementID  => index of the page that contains element with id elementID
	// #bookid/elementID/numberX => index of the page that contains element with id elementID PLUS numberX
	locationHashToPage : function(hash, pqp) {
		if (hash===undefined) hash=window.location.hash;
		if (hash=='#'+this.id+"/") return 0;
		hash = hash.slice(1).split("/");
		if (hash[0]!==this.id) return;
		if (hash.length===1) return 0;
		var page = parseInt(hash[1]);
		if (!isNaN(page)) return Math.max(page-1, 0);
		page = this.selectorToPage('#'+hash[1]);
		if (page===undefined) return 0;
		if (!isNaN(hash[2])) page += Math.max(parseInt(hash[2])-1, 0);
		return +page;
	}, // locationHashToPage

	// Converts a page index into a windows.location.hash
	// without sections : page index X => #bookid/pageIndexX
	// with    section  : page index X => #bookid/sectionID/offset-page-in-the-section
	pageToLocationHash : function(pageIndex) {
		var hash    = '',
			offset  = pageIndex+1,
			section = this.pageToSection(pageIndex);
		if (section) {
			hash   += '/'+section.id.replace('#','');
			offset -= section.page;
		}
		if (offset>1) hash += '/'+offset;
		return '#'+this.id+( hash || '/');
	}, // pageToLocationHash

	// return the pageIndex that contains the jquery selector
	selectorToPage : function(selector) {
		var e=$(selector, this.elem).closest('.wowbook-page');
		if (e.length) return +e.data('pageIndex');
	}, // selectorToPage

	getLocationHash : function(){
		return window.location.hash.slice(1);
	}, // getLocationHash

	locationEndsInHash : function(href){
		if (href===undefined) href= window.location.href;
		return href.lastIndexOf("#")==href.length-1;
	}, // locationEndsInHash


	//
	// Zoom
	//
	zoomSetup : function(){
		this._zoomOffset = { dx: 0, dy: 0 };
		this._cssZoom = this._cssZoom || 1;
		this.zoomLevel = 1;
		this.detectBestZoomMethod();
		this._isMobile = $.wowBook.utils.isMobile();
		this.zoomTouchSupport();
	}, // zoomSetup

	_zoomUpdateOnRAF: function(){
		if ( !this._zoomDataRAF ) return;
		var zoptions = $.extend({}, this._zoomDataRAF.options),
		    target = this._zoomDataRAF.options.offset;
		if (target) {
		    var currentOffset = this._zoomOffset,
		        deltaX = target.dx-currentOffset.dx,
		        deltaY = target.dy-currentOffset.dy;
			zoptions.offset = {
				dx : currentOffset.dx+deltaX*0.2,
				dy : currentOffset.dy+deltaY*0.2
			}
		}
		var level = this._zoomDataRAF.level || this.zoomLevel;
		if ( level!=this.zoomLevel ) {
		    level = this.zoomLevel+ (level-this.zoomLevel)*0.2;
		}
		zoptions.transform = true;
		this._zoom( level, zoptions )

		if (target && (Math.abs(deltaX)<1 && Math.abs(deltaY)<1) && (Math.abs(this.zoomLevel-level)<1)) {
			if (this._zoomDataRAF.callback) this._zoomDataRAF.callback.call(this);
			this._zoomDataRAF = null;
		}
	}, // _zoomUpdateOnRAF

	_zoom : function(level, options){
		if (!options) options={};

		var x = (options.x!=undefined ? options.x : this.pageWidth*this.currentScale),
		    y = options.y || 0;

		this._zoomOffset = options.offset || this.zoomFocusOffset( level, x, y );
		this.zoomLevel = level;
		var useTransform = options.transform || this.opts.zoomUsingTransform,
		    newLevel    = level*this.currentScale,
		    zoomFix     = $.browser.ie7 ? 1 : (useTransform ? this._cssZoom : newLevel),
		    zoomWindow  = this.zoomWindow,
		    zoomContent = this.zoomContent,
		    boundingBox = $(this.zoomBoundingBox),
			bbWidth  = boundingBox.outerWidth(),
			bbHeight = boundingBox.outerHeight();

		// zoomWindow with the same size and position than bounding box
		var zwo = zoomWindow.offset(),
		    zwp = zoomWindow.position(),
		    bbo = boundingBox[0]!==window ? boundingBox.offset() : { left: boundingBox.scrollLeft(), top: boundingBox.scrollTop() };
		zoomWindow.css({
			width  : bbWidth,
			height : bbHeight
		})
		var dLeft = bbo.left-zwo.left,
		    dTop = bbo.top-zwo.top;
		if (dLeft) {
			zoomWindow.css("marginLeft", dLeft);
			zoomContent.marginLeft = dLeft;
		}
		if (dTop) {
			zoomWindow.css("marginTop", dTop);
			zoomContent.marginTop = dTop;
		}
		var transform = "",
		    offsetX   = this._zoomOffset.dx/zoomFix,
		    offsetY   = this._zoomOffset.dy/zoomFix;

		if ($.wowBook.support.transform && (offsetX || offsetY)) {
			transform = $.wowBook.utils.translate( offsetX, offsetY);
		} else {
			zoomContent.css({ left: offsetX, top: offsetY });
		}

		if (useTransform) {
			var scale = newLevel/zoomFix;
			transform += this.opts.useScale3d ? "scale3d("+scale+","+scale+",1)"
			                                  : "scale("+scale+")"
		} else {
			this._cssZoom = newLevel;
			zoomContent.css('zoom', newLevel);
			zoomContent.css("marginLeft", -zoomContent.marginLeft/zoomFix );
			zoomContent.css("marginTop", -zoomContent.marginTop/zoomFix );
		}

		if ($.wowBook.support.transform) zoomContent.css('transform', transform);

		if (this.zoomLevel!==1) {
			if (!this.zoomed) {
				// zoom started now
				zoomContent.css("marginLeft", -zoomContent.marginLeft/zoomFix );
				zoomContent.css("marginTop", -zoomContent.marginTop/zoomFix );

				if (useTransform) zoomContent.css('transformOrigin', "0 0");

			}
			// zoom changing

		} else {
			// zoom finished
			this.zoomFinished();
		}

		this.zoomed = (level!==1);
		zoomContent.toggleClass('wowbook-draggable', this.zoomed);
		// FIXME: mover os toggles abaixo para o zoom?
		this.toggleControl("zoomIn",  this.zoomLevel==this.zoomMax );
		this.toggleControl("zoomOut", this.zoomLevel==this.zoomMin );

	}, // _zoom

	zoom : function(level, duration, options){
		this.uncurl(true);
		for(var i=0,l=this.pages.length;i<l;i++) if (this.pages[i].data('holdedAt')) return;

		if ($.isPlainObject(duration)) { options=duration; duration=options.duration; }
		if (!options) options={}

		if (level<=this.zoomMin && !options.resetting) return this.zoomReset(duration, options);
		if (level>this.zoomMax) level=this.zoomMax;
		if (level===this.zoomLevel && !options.force) return;

		if (duration==undefined) duration = this.opts.zoomDuration;
		if (duration==0) {
			this._zoom(level, options);
			if (options.callback) options.callback.apply(this)
			if (this.onZoom) this.onZoom(this);
			return;
		}

		var webkit = !this.opts.zoomUsingTransform &&  $.wowBook.support.transform;

		if (this._zoomAnimating) {
			$(this).stop();
			if (webkit) {
				this.zoomContent.css('transform', "" );

			}
		}

		this._zoomAnimating = this.zoomLevel;

		var book = this,
		    x = (options.x!=undefined ? options.x : this.pageWidth*this.currentScale),
		    y = options.y || 0;
		    o = { x: x, y: y, offset: { dx: 0, dy: 0 } },
		    initialOffset = $.extend( { dx: 0, dy: 0 }, this._zoomOffset ),
		    finalOffset   = options.offset || this.zoomFocusOffset( level, x, y ),
		    dx = finalOffset.dx-initialOffset.dx,
		    dy = finalOffset.dy-initialOffset.dy;

		if (webkit){
			o.transform = true;
			if (this._isMobile) {
				if (this.leftPage())  this.leftPage().css("-webkit-transform", "translateZ(0)" )
				if (this.rightPage()) this.rightPage().css("-webkit-transform", "translateZ(0)" )
			}
		}

		$(this).animate({ _zoomAnimating: level }, {
			duration : duration,
			easing   : options.easing || this.opts.zoomEasing,
			complete : function(){
				book._zoomAnimating = false;




				book._zoom( level )
				if (options.callback) options.callback.apply(this)
				if (book.onZoom) book.onZoom(book);
			},
			step:function(e, t){
				o.offset.dx = initialOffset.dx + dx*t.pos;
				o.offset.dy = initialOffset.dy + dy*t.pos;
				book._zoom( e, o )
			}
		})
	}, // zoom

	zoomFinished : function(){
		//zoomWindow.unbind('mousemove.wowbook').css({
		this.zoomWindow.css({
			overflow : 'visible',
			width  : this.zoomContent.width(),
			height : this.zoomContent.height(),
			marginLeft : 0,
			marginTop  : 0
		});
		this.zoomContent.css({
			left       : 0,
			top        : 0,
			marginLeft : 0,
			marginTop  : 0
		});
		this._zoomOffset = { dx: 0, dy: 0 };

	}, // zoomFinished

	zoomReset : function(duration, options){
		if ($.isPlainObject(duration)) { options=duration; duration=options.duration; }
		if (!options) options={}

		this._zoomDataRAF = null;
		options.offset = { dx: 0, dy: 0 };
		options.resetting = true;
		options.force = true;
		options.callback = function(){
			this.zoomContent.css({ left: 0, top: 0 });
			this.zoomed = false;
		}
		this.zoom(1, duration, options);
	}, // zoomReset

	zoomIn : function(step, options){
		if ($.isPlainObject(step)) { options=step; step=undefined }
		this.zoom(this.zoomLevel + (step || this.zoomStep), options);
	},

	zoomOut : function(step, options){
		if ($.isPlainObject(step)) { options=step; step=undefined }
		this.zoom(this.zoomLevel - (step || this.zoomStep), options);
	},

	zoomFocusOffset : function( newZoom, x, y, offset, currentZoom ){
		if (!offset) offset = this._zoomOffset || { dx: 0, dy: 0 };
		offset = $.extend({ dx: 0, dy: 0 }, offset);
		var dx = offset.dx || 0,
		    dy = offset.dy || 0,
		    f  = newZoom/(currentZoom || this.zoomLevel),
		    xt, yt;
		x  = x-dx; y = y-dy;
		xt = x*f;
		yt = y*f;
		offset.dx = dx -(xt-x)
		offset.dy = dy -(yt-y)
		return { dx: dx -(xt-x), dy: dy -(yt-y) };
	}, // zoomFocusOffset

	zoomTouchSupport : function(){
		if (!this.opts.touchEnabled) return;

		// for some reason, hammerjs isn't working with IE8/7
		// this is a workaround until the problem is fixed
		if ($.browser.ie8mode || $.browser.ie7) return this.zoomDragSupportForIE();

		var book = this,
		    bookOffset, dragStart, pinchStart;

		book._hammer = book.zoomContent.hammer(
			book.opts.touch
		).on("touch.wowbook", function(evt){
			book.zoomContent.addClass("wowbook-dragging");
		}).on("release.wowbook", function(evt){
			if (evt.gesture.changedLength!=0) return;
			book.zoomContent.removeClass("wowbook-dragging");
			var level = book.zoomLevel;
			if (( level < book.zoomMin ) ||
			    ( level == book.zoomMin && (book._zoomOffset.dx || book._zoomOffset.dy) )) {
				book.zoomReset();
			} else {
				book._zoom( level, { force: true, offset: book._zoomOffset });
			}
		}).on("drag.wowbook dragstart.wowbook dragend.wowbook", function(evt){
			if (!book.zoomed) return
			var gesture = evt.gesture;
			if (!gesture) return;
			pinchStart = null;
			var touchId = gesture.touches[0].identifier;
			if (!dragStart || touchId!=dragStart.touchId) {
				dragStart = {
					touchId : touchId,
					offset  : $.extend({}, book._zoomOffset),
					pageX : gesture.center.pageX,
					pageY : gesture.center.pageY
				}
			}

			if (evt.type=="dragend") {
				dragStart = null;
				return
			}
			var dx = dragStart.offset.dx + (gesture.center.pageX-dragStart.pageX),
			    dy = dragStart.offset.dy + (gesture.center.pageY-dragStart.pageY);

			book._zoomDataRAF = {
				level: book.zoomLevel,
				options: { force: true, offset: { dx: dx, dy: dy } }
			}

			gesture.preventDefault();
		})
		if (book.opts.pinchToZoom) {
			book._hammer.on("pinch.wowbook transformstart.wowbook transformend.wowbook", function(evt){
				var gesture = evt.gesture;
				if (!gesture) return;

				dragStart = null;
				var pageX = gesture.center.pageX, pageY = gesture.center.pageY;
				if (!pinchStart) {
					bookOffset = book.elem.offset();
					pinchStart = {
						level   : book.zoomLevel,
						pageX   : pageX,
						pageY   : pageY,
						x       : pageX-bookOffset.left,
						y       : pageY-bookOffset.top,
						offset  : $.extend({}, book._zoomOffset),
						useTransform : book.opts.zoomUsingTransform
					}
				}

				if (evt.type=="transformend"){
					pinchStart = null;
					return
				}
				var newLevel = pinchStart.level*gesture.scale;
				if (newLevel>book.zoomMax) newLevel=book.zoomMax;
				var offset = book.zoomFocusOffset( newLevel, pinchStart.x, pinchStart.y, pinchStart.offset, pinchStart.level );
				offset.dx += (pageX-pinchStart.pageX);
				offset.dy += (pageY-pinchStart.pageY);

				book._zoomDataRAF = {
					level: newLevel,
					options: { force: true, offset: offset }
				}

				gesture.preventDefault();
			})
		}
	}, // zoomTouchSupport

	// for some reason, hammerjs isn't working with IE8/7
	// this is a workaround until the problem is fixed
	zoomDragSupportForIE : function(){
		var book=this;
		var dragStart;

		var mousedownhandler =  function(evt){
			if (!book.zoomed) return;
			dragStart = {
				offset  : $.extend({}, book._zoomOffset),
				pageX : evt.pageX,
				pageY : evt.pageY
			}
			$(document)
			   .bind('mousemove.wowbook', mousemoveHandler)
			   .bind('mouseup.wowbook',   mouseupHandler);
			return false;
		} // mousedownhandler

		var mousemoveHandler =  function(evt){
			var dx = dragStart.offset.dx + (evt.pageX-dragStart.pageX),
			    dy = dragStart.offset.dy + (evt.pageY-dragStart.pageY);

			book._zoomDataRAF = {
				level: book.zoomLevel,
				options: { force: true, offset: { dx: dx, dy: dy } }
			}
			return false;
		} // mousemoveHandler

		var mouseupHandler =  function(e){
			var level = book.zoomLevel;
			if (( level < book.zoomMin ) ||
			    ( level == book.zoomMin && (book._zoomOffset.dx || book._zoomOffset.dy) )) {
				book.zoomReset();
			}
			$(document).unbind('mousemove.wowbook', mousemoveHandler);
			$(document).unbind('mouseup.wowbook',   mouseupHandler);
		} // mouseupHandler

		book.zoomContent.bind("mousedown.wowbook", mousedownhandler);
	}, // zoomDragSupportForIE


	// detect if we should use CSS zoom or CSS transform to zoom
	detectBestZoomMethod : function(supportTransform, supportZoom, ie8mode){
		if (supportTransform===undefined) supportTransform = $.wowBook.support.transform;
		if (supportZoom===undefined) supportZoom = $.wowBook.support.zoom;
		if (ie8mode===undefined) ie8mode = $.browser.ie8mode;
		var isWebkit = $.browser.chrome || $.browser.webkit || $.browser.safari || $.browser.opera;
		var useZoom  = isWebkit || ie8mode || !supportTransform;
		this.opts.zoomUsingTransform = !useZoom;
		return useZoom ? "zoom" : "transform";
	}, // detectZoomMethod


	//
	// Fullscreen
	//
	setupFullscreen : function(){
		if (_requestFullscreen) {
			var book=this,
			    changeEvents = "fullscreenchange mozfullscreenchange webkitfullscreenchange MSFullscreenChange ",
			    errorEvents = "fullscreenerror mozfullscreenerror webkitfullscreenerror MSFullscreenError ";
			changeEvents = changeEvents.replace(/ /g, ".wowbook ");
			errorEvents = errorEvents.replace(/ /g, ".wowbook ");
			this._fullscreenChangeHandler = function(){
				var fullscreenEnabled = fullscreenElement();
				$(book.opts.fullscreenElement).toggleClass("fullscreen", fullscreenEnabled);
				book.elem.toggleClass("fullscreen", fullscreenEnabled);
				book.toggleControl("fullscreen", fullscreenEnabled);
			}
			$(document).on(changeEvents, this._fullscreenChangeHandler);

			this._fullscreenErrorHandler = function(){
				if (book.opts.onFullscreenError) book.opts.onFullscreenError.apply(this, arguments)
			}
			$(document).on(errorEvents, this._fullscreenErrorHandler);
		} else {
			$(this.opts.controls.fullscreen).hide();
		}
	}, // setupFullscreen

	enterFullscreen : function(elem){
		requestFullscreen($(elem || this.opts.fullscreenElement)[0]);
	}, // enterFullscreen

	exitFullscreen : function(){
		exitFullscreen();
	}, // enterFullscreen

	toggleFullscreen : function(){
		fullscreenElement() ? this.exitFullscreen() : this.enterFullscreen();
	}, // toggleFullscreen


	//
	// Book Shadow
	//
	positionBookShadow : function(){
		var pageLength = this.pages.length,
		    show = !!(this.opts.bookShadow && pageLength && !(pageLength<3 && this.holdedPage));
		this.bookShadow.toggle(show);
		if (!show) return;

		var pw  = this.pageWidth,
		    hbp = this.holdedPageBack,
		    liftingLastPageOnLeft  = !!hbp && hbp.onRight && (hbp.pageIndex == (this.rtl? pageLength-1 : 0));
		    liftingLastPageOnRight = !!hbp && hbp.onLeft  && (hbp.pageIndex == (this.rtl? 0 : pageLength-1));
		    noPageOnLeft   = !this.leftPage()  || liftingLastPageOnLeft,
		    noPageOnRight  = !this.rightPage() || liftingLastPageOnRight,
			onePageVisible = noPageOnLeft != noPageOnRight;
		if (noPageOnLeft && noPageOnRight) { this.bookShadow.hide(); return; }

		var correction = this.opts.zoomUsingTransform ? this.currentScale*this.zoomLevel : 1;
		this.bookShadow.css({
			left  : ((noPageOnLeft ? pw : 0)) + this.pagesContainer.position().left/correction,
			width : onePageVisible ? pw : pw*2
		});
	}, // positionBookShadow


	//
	// Page flip sound
	//
	playFlipSound : function(){
		if (!this.flipSound) return;
		var c=this.opts.onPlayFlipSound;
		if ($.isFunction(c) && (c(this)===false)) return;
		if (!this.audio) this.audio = this.createAudioPlayer();
		if (this.audio && this.audio.play) this.audio.play();
	}, // playFlipSound

	toggleFlipSound : function(enabled){
		if (!arguments.length) enabled = !this.flipSound
		this.flipSound = enabled
		this.toggleControl("flipSound", !enabled)
	}, // toggleFlipSound

	createAudioPlayer : function(path, files){
		if (!path)  path  = this.opts.flipSoundPath;
		if (!files) files = this.opts.flipSoundFile;
		var srcs = [];
		for (var i=0, l=files.length; i<l; i++)
			srcs.push('<source src="'+path+files[i]+'">');
		return $('<audio preload>'+srcs.join('')+'</audio>')[0];
	}, // createAudioPlayer


	//
	// Touch
	//
	_untouch : function(e){
		return (e.originalEvent.touches && e.originalEvent.touches[0]) || e;
	},

	touchSupport:function(){
		var book=this;
		book.elem.bind('touchstart.wowbook', function(e){
			var touches = e.originalEvent.touches;
			if (touches.length>1) return;
			book._touchStarted = {
				x         : touches[0].pageX,
				y         : touches[0].pageY,
				timestamp : e.originalEvent.timeStamp,
				inHandle  : $(e.target).hasClass('wowbook-handle')
			}
			if (book._touchStarted.inHandle) book.pageEdgeDragStart( book._untouch(e) );
		});
		$(document).on('touchmove.wowbook', function(e){
			if (!book._touchStarted) return;
			var touches = e.originalEvent.touches;
			book._touchEnded = {
				x         : touches[0].pageX,
				y         : touches[0].pageY,
				timestamp : e.originalEvent.timeStamp
			}
			if (book._touchStarted.inHandle) return book.pageEdgeDrag( book._untouch(e) );
			var dx = book._touchEnded.x-book._touchStarted.x;
			var dy = book._touchEnded.y-book._touchStarted.y;
			if (Math.abs(dx) > 20) e.preventDefault();
			e.preventDefault();
		});
		$(document).on('touchend.wowbook touchcancel.wowbook', function(e){
			if (!book._touchStarted) return;
			if (!book._touchEnded && $(e.target).hasClass('wowbook-handle')){
				var g = $(e.target).data('corner');
				if (g==='r') book.advance();
				if (g==='l') book.back();
			}

			var _touchStarted = book._touchStarted,
			    _touchEnded   = book._touchEnded || book._touchStarted;
			book._touchStarted = null;
			book._touchEnded   = null;
			if (book.zoomed) return;
			if (_touchStarted.inHandle) {
				book.pageEdgeDragStop({ pageX: _touchEnded.x });
				return false;
			}
			var dx = _touchEnded.x-_touchStarted.x;
			var dy = _touchEnded.y-_touchStarted.y;
			var dt = _touchEnded.timestamp-_touchStarted.timestamp;
			if (Math.abs(dx)<20 || dt>200) return
			if (Math.abs(dx) > Math.abs(dy)) {
				if (dx<0) book.advance()
				else book.back()
				return false;
			}
		});
	}, // touchSupport

	//
	// Page edge drag
	//
	pageEdgeDragStart : function(e){
		if (this.zoomed) return;
		if ((this.animating && !this.curledPage) || (!$(e.target).hasClass('wowbook-handle'))) return false;
		var book = this,
		    o    = book.elem.offset();
		book.elem.addClass("wowbook-unselectable");
		book.mouseDownAtLeft  = ((e.pageX-o.left)/this.currentScale < book.pageWidth);
		book.pageGrabbed      = (book.mouseDownAtLeft ? book.leftPage() : book.rightPage());

		if (!book.pageGrabbed) return false;
		this.uncurl(true)
		book.pageGrabbedOffset = book.pageGrabbed.offset();
		if (this.opts.zoomUsingTransform) {
			book.pageGrabbedOffset.left = book.pageGrabbedOffset.left/this.currentScale;
			book.pageGrabbedOffset.top  = book.pageGrabbedOffset.top/ this.currentScale;
		}


		var x = (e.pageX/this.currentScale - this.pageGrabbedOffset.left),
		    y = (e.pageY/this.currentScale - this.pageGrabbedOffset.top);

		this.stopAnimation(false)
		var corner = (book.mouseDownAtLeft ? "l" : "r");
		this.holdPage(this.pageGrabbed, x, y);
		this.flip(x, y, this.pageGrabbed, { corner: corner });

		$(document)
		   .bind('mousemove.wowbook', function(e){ return book.pageEdgeDrag(e) })
		   .bind('mouseup.wowbook',   function(e){ return book.pageEdgeDragStop(e) });
		return false;
	}, // pageEdgeDragStart

	pageEdgeDrag : function(e){
		var x = (e.pageX/this.currentScale - this.pageGrabbedOffset.left),
		    y = (e.pageY/this.currentScale - this.pageGrabbedOffset.top);

		var corner = (this.mouseDownAtLeft ? "l" : "r");

		this.stopAnimation(false)
		this.flip(x, y, this.pageGrabbed, { corner: corner, dragging: true});

		return false;
	}, // pageEdgeDrag

	pageEdgeDragStop : function(e){
		var book = this,
		    o    = book.elem.offset(),
		    mouseUpAtLeft = ((e.pageX-o.left)/this.currentScale < book.pageWidth);

		book.elem.removeClass("wowbook-unselectable");

		if (!this._cantStopAnimation) this.stopAnimation(false);

		if (book.mouseDownAtLeft && !mouseUpAtLeft) {
			this.rtl ? book.advance() : book.back();
		} else if (!book.mouseDownAtLeft && mouseUpAtLeft) {
			this.rtl ? book.back() : book.advance();
		} else {
			book.releasePage(book.pageGrabbed, true);
		}

		$(document).unbind('mousemove.wowbook mouseup.wowbook');
	}, // pageEdgeDragStop

	//
	// Curl
	//
	curl : function(page, bottom){
		if (this.curledPage || this.holdedPage || this.zoomed) return

		if (page==undefined) page = this.currentPage
		if (typeof page=="number" || typeof page=="string") page=this.pages[+page];
		if (!page || page.isCurled) return
		page.isCurled = true
		this.curledPage = page

		var onleft = this.pageIsOnTheLeft(page.pageIndex),
		    x0 = onleft  ? 0 : this.pageWidth,
		    x1 = x0 + this.opts.curlSize*(onleft ? 1 : -1),
		    y0 = !bottom ? 2 : this.pageHeight-1,
		    y1 = y0 + this.opts.curlSize*(!bottom ? 1 : -1),
		    corner = (bottom ? "b" : "t") + (onleft ? "l" : "r");

		this.flip({
			from     : [x0, y0],
			to       : [x1, y1],
			corner   : corner,
			page     : page,
			duration : 400
		})
	}, // curl

	uncurl : function(page, dontAnimate){
		if (!this.curledPage) return

		if (page==true) dontAnimate=true, page=undefined;
		if (page==undefined) page = this.curledPage || this.currentPage
		if (typeof page=="number" || typeof page=="string") page=this.pages[+page];
		if (!page.isCurled) return

		this.stopAnimation(false)
		this.releasePage(page, !dontAnimate, undefined, 400)
		page.isCurled = false
		this.curledPage = null
	}, // uncurl


	//
	// Thumbnails
	//
	initThumbnails: function(){
		var opts = this.opts;
		this.thumbnails = [];
		this.thumbnailsContainer = $("<div class='wowbook-thumbnails'>").append(
			"<div class='wowbook-wrapper'>"+
			"<div class='wowbook-back wowbook-button' />"+
			"<div class='wowbook-clipper'><ul></ul></div>"+
			"<div class='wowbook-next wowbook-button' />"+
			"</div>")
			.css('display', 'none')
			.css('transform', 'translateZ(0)')
			.appendTo($(opts.thumbnailsParent));
		var container = this.thumbnailsContainer;
		this.thumbnailsList    = container.find("ul");
		this.thumbnailsClipper = container.find(".wowbook-clipper");
		if (opts.thumbnailsContainerWidth) container.width( opts.thumbnailsContainerWidth )
		if (opts.thumbnailsContainerHeight) container.height( opts.thumbnailsContainerHeight )

		var position = opts.thumbnailsPosition;
		if (position=="left" || position=="right"){
			opts.thumbnailsVertical = true
			if (position=="right") container.css({
				position: 'absolute',
				left: 'auto',
				right: '0px' })
		}
		if (position=="top" || position=="bottom"){
			opts.thumbnailsVertical = false
			if (position=="bottom") container.css({
				position: 'absolute',
				top: 'auto',
				bottom: '0px' })
		}
		container.addClass(opts.thumbnailsVertical ? 'wowbook-vertical' : 'wowbook-horizontal')

		var book=this;

		// Buttons
		var dimension = opts.thumbnailsVertical ? "height" : "width";

		this.thumbnailsBackButton = container.find('.wowbook-back.wowbook-button').click(function(){
			book._moveThumbnailsList( book.thumbnailsClipper[dimension]() );
		})
		this.thumbnailsNextButton = container.find('.wowbook-next.wowbook-button').click(function(){
			book._moveThumbnailsList( -book.thumbnailsClipper[dimension]() );
		})

		// when user click the buttons, the thumbnails slides.
		// ipad need this for a more smooth movement
		this.thumbnailsClipper.css('transform', 'translateZ(0)')

	}, // thumbnails

	destroyThumbnails : function(){
		this.thumbnailsContainer && this.thumbnailsContainer.remove()
		this.thumbnailsContainer = null
		this.thumbnails = null
	}, // destroyThumbnails

	createThumbnails : function(){
		if (!this.thumbnails) this.initThumbnails()
		var thumb,
		    config = this.thumbnailConfig();
		this.thumbnails = [];
		for(var i=0, l=this.pages.length; i<l; i++){
			thumb = this.createThumbnail(i, config);
			this.thumbnailsList.append( thumb );
			this.thumbnails.push( thumb )
		}
		if (this.rtl){
			var thumbs = this.thumbnailsList.children();
			thumbs.eq(0).addClass("wowbook-right").removeClass("wowbook-left")
			for(var i=1, l=thumbs.length; i<l; i+=2) thumbs.eq(i).insertAfter( thumbs.eq(i+1) );
		}

		var tc = this.thumbnailsContainer;
		if (!tc.width()) tc.width( config.width*2 );

	}, // createThumbnails

	thumbnailConfig : function(){
		var config = {},
		    // IE7 makes a empty div have the height of line-height, hence the lineheight:0
	        fakeThumb = $('<div class="wowbook-thumbnail" style="display:none;position:absolute;line-height:0px;font-size:0px;">').prependTo(this.thumbnailsContainer),
		    // IE7 bug makes the height of the empty div=2. Since nobody wants a thumbnail
		    // with 2 pixels height, when this happens we consider that it probably means height = 0
		    thumbHeight = this.opts.thumbnailHeight || (fakeThumb.height()<=2 ? 0 : fakeThumb.height()),
		    thumbWidth  = this.opts.thumbnailWidth  || fakeThumb.width(),
		    scale = thumbWidth/this.pageWidth ||
		            thumbHeight/this.pageHeight || this.opts.thumbnailScale;
		fakeThumb.remove();
		config.width  = thumbWidth  || this.pageWidth*scale;
		config.height = thumbHeight || this.pageHeight*scale;
		config.cloneCSS = {
			display         : 'block',
			left            : 0,
			top             : 0,
			position        : 'relative',
			transformOrigin : "0 0"
		};
		if ($.wowBook.support.transform) {
			config.cloneCSS.transform = "scale("+scale+")"
		} else {
			config.cloneCSS.zoom = scale;
		}
		return config
	}, // thumbnailConfig

	createThumbnail : function(pageIndex, config){
		var page = this.pages[pageIndex];
		if (!page) return
		if (!config) config=this.thumbnailConfig();

	    var thumb = $('<li class="wowbook-thumbnail"><div class="wowbook-overlay">')
			.addClass( this.pageIsOnTheLeft(pageIndex) ? "wowbook-left" : "wowbook-right" )
			.css({ width : config.width, height : config.height });

		if (this.opts.thumbnailsSprite) {
			thumb.css('background', 'url('+this.opts.thumbnailsSprite+') no-repeat 0px -'
			                        +pageIndex*config.height+"px")
		} else {
			var clonedPage = page.clone();
			if (clonedPage.hasClass("wowbook-page-holded")) {
				this.resetPage(clonedPage);
				clonedPage.find('.wowbook-fold-gradient-container').remove();
			}
			clonedPage.css(config.cloneCSS);
			thumb.prepend(clonedPage)
		}

		// click
		var book=this;
		thumb.click(function(){ book.gotoPage(pageIndex) })

		return thumb;
	}, // createThumbnail

	updateThumbnail : function(index, config){
		if (!this.thumbnails) return;
		var thumb = this.thumbnails[index]
		if (!thumb) return
		var newthumb = this.createThumbnail(index, config)
		if (!newthumb) return
		if (!this.opts.thumbnailsSprite) {
			thumb.children(":not(.wowbook-overlay)").replaceWith( newthumb.children(":not(.wowbook-overlay)") )
		}
		thumb.width( newthumb.width() )
		thumb.height( newthumb.height() )
	}, // updateThumbnail

	updateThumbnails : function(){
		if (!this.thumbnails) { this.createThumbnails(); return }
		var config = this.thumbnailConfig();
		for(var i=0, l=this.pages.length; i<l; i++){
			this.updateThumbnail(i, config);
		}
		var tc = this.thumbnailsContainer;
		if (!tc.width()) tc.width( config.width*2 );
	}, // updateThumbnails

	_moveThumbnailsList : function(offset, options){
		var currentPos = this.thumbnailsList.position()[this.opts.thumbnailsVertical ? "top" : "left"];
		this._setThumbnailsListPosition(currentPos+offset, options);
	}, // _moveThumbnailsList

	_setThumbnailsListPosition : function(position, options){
		var vertical  = this.opts.thumbnailsVertical,
		    dimension = vertical ? "height" : "width",
		    props     = {};

		var clipperSize = this.thumbnailsClipper[dimension](),
		    minpos = -this.thumbnailsList[dimension]()+clipperSize;

		if (position < minpos ) position = minpos;
		if (position > 0) position = 0;
		this.thumbnailsBackButton.toggleClass("wowbook-disabled", position==0      || minpos>0);
		this.thumbnailsNextButton.toggleClass("wowbook-disabled", position==minpos || minpos>0);
		props[vertical ? "top" : "left"] = position;
		this.thumbnailsList.animate(props, options!=undefined ? options : this.opts.thumbnailsAnimOptions );
	}, // _setThumbnailsListPosition

	showThumbnail : function(thumbIndex, duration){
		if (!this.thumbnails || !this.thumbnailsContainer.is(":visible")) return;
		if (thumbIndex==undefined) thumbIndex = this.currentPage;
		if (thumbIndex>0 && this.pageIsOnTheRight(thumbIndex)) thumbIndex--;

		var vertical  = this.opts.thumbnailsVertical,
		    prop      = vertical ? "top" : "left",
		    dimension = vertical ? "height" : "width";

		var thumb         = this.thumbnails[thumbIndex],
		    clipper       = this.thumbnailsClipper,
		    targetPos     = clipper[dimension]()/2-(thumb[dimension]()/(vertical ? 2 : 1) ),
		    thumbPos      = thumb.offset()[prop]-clipper.offset()[prop];

		this._moveThumbnailsList(targetPos-thumbPos, duration);
	}, // showThumbnail

	showThumbnails : function(duration){
		if (!this.thumbnails || !this.thumbnails.length) this.createThumbnails()
		this.thumbnailsContainer.fadeIn(duration!=undefined ? duration : this.opts.thumbnailsAnimOptions)
		this.showThumbnail(undefined, 0);
	},

	hideThumbnails : function(duration){
		this.thumbnailsContainer.fadeOut(duration!=undefined ? duration : this.opts.thumbnailsAnimOptions)
	},

	toggleThumbnails : function(duration){
		$(this.thumbnailsContainer).is(':visible') ? this.hideThumbnails(duration) : this.showThumbnails(duration)
	},



	//
	// Controls
	//
	controllify : function(controls){
		var book=this;
		$(controls.zoomIn   ).on("click.wowbook", function(){ book.zoomIn({});  return false });
		$(controls.zoomOut  ).on("click.wowbook", function(){ book.zoomOut({}); return false });
		$(controls.next     ).on("click.wowbook", function(){ book.advance(); return false });
		$(controls.back     ).on("click.wowbook", function(){ book.back();    return false });
		$(controls.first    ).on("click.wowbook", function(){ book.gotoPage(0); return false });
		$(controls.last     ).on("click.wowbook", function(){ book.gotoPage(book.pages.length-1); return false });
		$(controls.slideShow).on("click.wowbook", function(){ book.toggleSlideShow(); return false });
		$(controls.flipSound).on("click.wowbook", function(){ book.toggleFlipSound(); return false });
		$(controls.thumbnails).on("click.wowbook", function(){ book.toggleThumbnails(); return false });
		$(controls.fullscreen).on("click.wowbook", function(){ book.toggleFullscreen(); return false });
	},

	toggleControl : function(control, state){
		control = this.opts.controls[control];
		if (control) $(control).toggleClass('wowbook-disabled', state);
	} // toggleControl

} // Book methods

//
// Defaults
//
$.wowBook.defaults = {
	width                 : 500,
	height                : 300,
	startPage             : 0,
	hardcovers            : false,
	hardPages             : false,
	centeredWhenClosed    : false,
	doublePages           : '.double',

	responsive            : false,
	scaleToFit            : "",
	onResize              : null, // callback

	fullscreenElement     : document.documentElement,
	onFullscreenError     : null,

	use3d                 : true,
	perspective           : 2000,
	useTranslate3d        : 'mobile',
	useScale3d            : true,

	bookShadow            : true,
	gutterShadow          : true,
	shadowThreshold       : 20,
	shadows               : true,
	foldGradient          : true,
	foldGradientThreshold : 20,

	pageNumbers           : true,
	firstPageNumber       : 1,
	numberedPages         : false,

	deepLinking           : true,
	updateBrowserURL      : true,

	curl                  : true,
	curlSize              : 40,

	slideShow             : false,
	slideShowDelay        : 1000,
	pauseOnHover          : true,

	touchEnabled          : true,
	mouseWheel            : false,
	handleWidth           : false,
	handleClickDuration   : 300,
	turnPageDuration      : 1000,
	turnPageDurationMin   : 300,
	forceBasicPage        : false,
	sections              : '.wowbook-section',



	zoomLevel             : 1,
	zoomMax               : 2,
	zoomMin               : 1,
	zoomBoundingBox       : window,
	zoomStep              : 0.05,
	zoomDuration          : 200,
	zoomEasing            : "linear",
	onZoom                : null,
	pinchToZoom           : true,

	flipSound             : true,
	flipSoundFile         : ['page-flip.mp3', 'page-flip.ogg'],
	flipSoundPath         : './wow_book/sound/',
	onPlayFlipSound       : null,

	keyboardNavigation    : {
	                          back: 37,
	                          advance: 39
	                        },
	clipBoundaries        : true,
	controls              : {},
	onShowPage            : null,
	onHoldPage  	      : null,
	onReleasePage         : null,

	thumbnails : false,
	thumbnailsParent : "body",
	thumbnailScale   : 0.2,
	thumbnailWidth   : null,
	thumbnailHeight  : null,
	thumbnailsPosition : null, // 'left', 'right', 'top' or 'bottom'
	thumbnailsVertical : true, // or false to get horizontal thumbnails
	thumbnailsContainerWidth  : null,
	thumbnailsContainerHeight : null,
	thumbnailsSprite : null,
	thumbnailsAnimOptions : { }
}; // $.wowBook.defaults


if (typeof QUnit != "undefined") $.wowBook.wowBook = wowBook;

//
//  Utilities
//

/* paul irish http://www.paulirish.com/2011/requestanimationframe-for-smart-animating */
window.raf = (function(){
	return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame
	 || function(callback){ window.setTimeout(callback, 1000 / 60) }
})();

// Are we using IE in IE8 documentMode ? YES, i know it sucks, but there's a special case (aka bug)
// in IE8 that i did not find another way around  besides using browser detection.
// Same reason for IE7.
$.browser.ie8mode = ($.browser.msie && document.documentMode==8);
$.browser.ie7 = ($.browser.msie && ($.browser.version==7 || document.documentMode==7));

/*
 * rotatePoint
 *
 * rotate a point{x,y}
 *
 * params
 * 		point : object {x: number, y:number}
 * 		angle : number, angle in radians to rotate the point
 */
function rotatePoint(point, angle) {
	var c=Math.cos(angle),s=Math.sin(angle);
	return { x : c*point.x - s*point.y,
	         y : s*point.x + c*point.y }
} // rotatePoint

// returns true if element elem is visible (inside the browser viewport)
function isInViewPort(elem) {
	var viewportHeight = $(window).height(),
		offset = elem.offset(),
		top    = $(window).scrollTop();
	return (offset.top>top) && (offset.top+elem.height() < top+viewportHeight);
} // isInViewPort


// set width and height of element. if CSS box-sizing is not supported,
// make manually the equivalent of CSS box-sizing: border-boxSizingBorderBox
function boxSizingBorderBox(elem, width, height) {
	var pw=0, ph=0;
	if (!$.wowBook.support.boxSizing) {
		var bw = bordersWidth(elem);
		pw = parseFloat(elem.css('paddingLeft'))+parseFloat(elem.css('paddingRight'))+
			 bw.left+bw.right;
		ph = parseFloat(elem.css('paddingTop'))+parseFloat(elem.css('paddingBottom'))+
			 bw.top+bw.bottom;
	}
	elem.css('width', width-pw);
	elem.css('height', height-ph);
} // boxSizingBorderBox

//
// borderWidth for ie sometimes returns strings for border width
//
var damnIE = ($.browser.msie && $.browser.version<9) ? 1 : 0,
	borderWidths = { thin: 2-damnIE, medium: 4-damnIE, thick: 6-damnIE };

function bordersWidth(e) {
	var t;
	return {
        top    : (e.css('borderTopStyle')=='none' ? 0 : (borderWidths[t=e.css('borderTopWidth')] || parseFloat(t))),
        right  : (e.css('borderRightStyle')=='none' ? 0 : (borderWidths[t=e.css('borderRightWidth')] || parseFloat(t))),
        bottom : (e.css('borderBottomStyle')=='none' ? 0 : (borderWidths[t=e.css('borderBottomWidth')] || parseFloat(t))),
        left   : (e.css('borderLeftStyle')=='none' ? 0 : (borderWidths[t=e.css('borderLeftWidth')] || parseFloat(t)))
    };
};

// Fullscreen utils -based on code by mozilla
var doc = window.document;
var docEl = doc.documentElement;

var _requestFullscreen = docEl.requestFullscreen || docEl.mozRequestFullScreen ||
                         docEl.webkitRequestFullscreen || docEl.msRequestFullscreen,
    requestFullscreen  = function(elem){ return _requestFullscreen.call(elem || docEl) },
    _exitFullscreen    = doc.exitFullscreen || doc.mozCancelFullScreen ||
                         doc.webkitExitFullscreen || doc.msExitFullscreen,
    exitFullscreen     = function(elem){ return _exitFullscreen.call(doc) },
    fullscreenElement  = function(){ return doc.fullscreenElement || doc.mozFullScreenElement ||
                                           doc.webkitFullscreenElement || doc.msFullscreenElement };

$.wowBook.utils = {
	translate : function translate(x,y,z){
		return $.wowBook.useTranslate3d ?
		           "translate3d("+x+"px, "+y+"px, "+(z||0)+"px) "
		         : "translate("+x+"px, "+y+"px) "
	}, // translate

	isMobile : function(){
		return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
	} // isMobile

} // $.wowBook.utils

})(jQuery);




/*! Copyright (c) 2011 Brandon Aaron (http://brandonaaron.net)
 * Licensed under the MIT License (LICENSE.txt).
 *
 * Thanks to: http://adomas.org/javascript-mouse-wheel/ for some pointers.
 * Thanks to: Mathias Bank(http://www.mathias-bank.de) for a scope bug fix.
 * Thanks to: Seamus Leahy for adding deltaX and deltaY
 *
 * Version: 3.0.6
 *
 * Requires: 1.2.2+
 */

(function($) {

var types = ['DOMMouseScroll', 'mousewheel'];

if ($.event.fixHooks) {
    for ( var i=types.length; i; ) {
        $.event.fixHooks[ types[--i] ] = $.event.mouseHooks;
    }
}

$.event.special.mousewheel = {
    setup: function() {
        if ( this.addEventListener ) {
            for ( var i=types.length; i; ) {
                this.addEventListener( types[--i], handler, false );
            }
        } else {
            this.onmousewheel = handler;
        }
    },

    teardown: function() {
        if ( this.removeEventListener ) {
            for ( var i=types.length; i; ) {
                this.removeEventListener( types[--i], handler, false );
            }
        } else {
            this.onmousewheel = null;
        }
    }
};

$.fn.extend({
    mousewheel: function(fn) {
        return fn ? this.bind("mousewheel", fn) : this.trigger("mousewheel");
    },

    unmousewheel: function(fn) {
        return this.unbind("mousewheel", fn);
    }
});


function handler(event) {
    var orgEvent = event || window.event, args = [].slice.call( arguments, 1 ), delta = 0, returnValue = true, deltaX = 0, deltaY = 0;
    event = $.event.fix(orgEvent);
    event.type = "mousewheel";

    // Old school scrollwheel delta
    if ( orgEvent.wheelDelta ) { delta = orgEvent.wheelDelta/120; }
    if ( orgEvent.detail     ) { delta = -orgEvent.detail/3; }

    // New school multidimensional scroll (touchpads) deltas
    deltaY = delta;

    // Gecko
    if ( orgEvent.axis !== undefined && orgEvent.axis === orgEvent.HORIZONTAL_AXIS ) {
        deltaY = 0;
        deltaX = -1*delta;
    }

    // Webkit
    if ( orgEvent.wheelDeltaY !== undefined ) { deltaY = orgEvent.wheelDeltaY/120; }
    if ( orgEvent.wheelDeltaX !== undefined ) { deltaX = -1*orgEvent.wheelDeltaX/120; }

    // Add event and delta to the front of the arguments
    args.unshift(event, delta, deltaX, deltaY);

    return ($.event.dispatch || $.event.handle).apply(this, args);
}

})(jQuery);


//
// Hooks in jQuery for 'transform' and 'transformOrigin'
//
(function($){
	if (!$.cssHooks){
		alert("jQuery 1.4.3+ is needed for this plugin to work");
		return;
	}
	var div = document.createElement('div'),
	    prefixes = ['O', 'ms', 'Webkit', 'Moz'];

	// test different vendor prefixes of this property
	function checkSupportFor(propertyName) {
		if (propertyName in div.style) return $.wowBook.support[propertyName] = propertyName;
		var i = prefixes.length,
			p,
			sufix = propertyName.charAt(0).toUpperCase() + propertyName.substr(1);
		while (i--) {
			p = prefixes[i]+sufix;
			if (p in div.style) return $.wowBook.support[propertyName] = p;
		}
	} // checkSupportFor
	checkSupportFor('transform');
	checkSupportFor('transformOrigin');
	checkSupportFor('boxSizing');
	checkSupportFor('zoom');
	// IE7 support boxSizing, but doesn't support border-box.
	// "document.documentMode" is undefined in IE<=7, and is 7(or 5) in IE8+ but with in document mode<=7
	// the line below means "support.boxSizing = false if is IE7- or IE8+ in documentMode<8"
	if ($.wowBook.support.boxSizing && document.documentMode<8) $.wowBook.support.boxSizing = false;

	div = null;
	$.each(["transform", "transformOrigin"], function(i,v){
		if ($.wowBook.support[v] && $.wowBook.support[v]!==v && !$.cssHooks[v]){
			$.cssHooks[v] = {
				get: function(elem, computed, extra){
					return $.css( elem, $.wowBook.support[v] );
				},
				set: function(elem, value){
					elem.style[$.wowBook.support[v]] = value;
				}
			};
		}
	});

	// cssClasses : array
	$.wowBook.applyAlphaImageLoader = function(cssClasses) {
		var filename, i, l, classname,
		    style = '',
		    part1 = "{background:none; filter : progid:DXImageTransform.Microsoft.AlphaImageLoader(src='",
		    part2 = "', sizingMethod='scale'); } ",
		    dummy = $("<div style='display:none'></div>").appendTo('body');
		for (i=0,l=cssClasses.length; i<l; i++){
			classname = cssClasses[i];
			dummy.addClass(classname);
			filename = dummy.css('background-image').match(/^url\("(.*)"\)$/);
			if (!filename) continue;
			style += '.'+classname+part1+filename[1]+part2;
			dummy.removeClass(classname);
		}
		$('body').append("<style>"+style+"</style>");
	} // applyAlphaImageLoader

})(jQuery);
