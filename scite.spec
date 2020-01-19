%define		_version	430
Name:		scite
Version:	4.3.0
Release:	1
Summary:	SCIntilla based GTK3 text editor
License:	MIT
Group:		Editors
Source0:	http://download.sourceforge.net/scintilla/%{name}%{_version}.tgz

Url:		http://www.scintilla.org/SciTE.html

BuildRequires:	gtk+3-devel
BuildRequires:	desktop-file-utils

Requires:       gtk+3.0

%description
SciTE is a SCIntilla based Text Editor. Originally built to demonstrate
Scintilla, it has grown to be a generally useful editor with facilities for
building and running programs.

%prep
%setup -q -c

%build
%make OPTFLAGS="%{optflags}" GTK3=1 -C scintilla/gtk
%make OPTFLAGS="%{optflags}" GTK3=1 -C scite/gtk
#%make OPTFLAGS="%{optflags}" -C scintilla/gtk
#%make OPTFLAGS="%{optflags}" -C scite/gtk

%install
rm -rf %{buildroot}
%make_install GTK3=1 -C scite/gtk
ln -s SciTE %{buildroot}%{_bindir}/scite

# include man-page
mkdir -p %{buildroot}%{_mandir}/man1/
mv scite/doc/scite.1 %{buildroot}%{_mandir}/man1/

%files
%doc scite/README scite/License.txt
%{_mandir}/man1/scite.1*
%{_bindir}/SciTE
%{_bindir}/scite
%{_datadir}/scite/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*


%changelog

* Wed Sep 12 2012 matteo <matteo> 3.2.2-1.mga3
+ Revision: 292471
- new version

* Tue May 01 2012 matteo <matteo> 3.1.0-1.mga2
+ Revision: 234439
- new version
  - upstream includes fix to scroll mask bug
  - few other bugs fixed

* Fri Apr 13 2012 matteo <matteo> 3.0.4-1.mga2
+ Revision: 230564
- deleted wrong patch of the gtk makefile
- fixed makeinstall_std arguments
- spec file cleaned
- fixed gtk makefile bug not allowing desktop file installation
- added desktop file patch
- fixed mouse wheel scroll bug
- new version
  - built against gtk3 rather than gtk2
- new version

* Wed Sep 28 2011 matteo <matteo> 2.29-1.mga2
+ Revision: 149694
- upgrade to 2.29
- replaced commands with macros
- imported package scite
