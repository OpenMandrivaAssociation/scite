%define name 	scite
%define version 1.71
%define release %mkrel 1

%define scitever %(echo %{version} | sed -e 's/\\.//')

Summary: 	GTK text editor based on scintilla
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Editors
Url: 		http://www.scintilla.org/SciTE.html
Source: 	scite%scitever.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires: 	gtk+2-devel pkgconfig

%description
SciTE is a GTK based single-document editor.  While its features are
limited, its main purpose is to show off scintilla, an extensible
text highlighting and formatting engine.

%prep
%setup -q -n scite

%build
cd ../scintilla/gtk
perl -p -i -e "s/-Os/$RPM_OPT_FLAGS/g" makefile
make GTK2=1
cd $RPM_BUILD_DIR/scite/gtk
perl -p -i -e "s/-Os/$RPM_OPT_FLAGS/g" makefile
perl -p -i -e 's/netscape/www-browser/g' ../src/Embedded.properties
perl -p -i -e 's/netscape/www-browser/g' ../src/html.properties
perl -p -i -e 's/netscape/www-browser/g' ../src/SciTEGlobal.properties
make GTK2=1

%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
mkdir -p $RPM_BUILD_ROOT/%_datadir/pixmaps
mkdir -p $RPM_BUILD_ROOT/%_datadir/gnome/apps/Applications
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
cp bin/SciTE $RPM_BUILD_ROOT/%_bindir
cp src/*.properties $RPM_BUILD_ROOT/%_datadir/%name
cp gtk/SciTE.desktop $RPM_BUILD_ROOT/%_datadir/gnome/apps/Applications
cp gtk/Sci48M.png $RPM_BUILD_ROOT/%_datadir/pixmaps
cp doc/%name.1 $RPM_BUILD_ROOT/%_mandir/man1

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="SciTE"\
needs="x11"\
section="More Applications/Editors"\
title="SciTE"\
icon="editors_section.png"\
longtitle="Scintilla Text Editor"
EOF

%clean
rm -fr $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc doc/*
%_bindir/SciTE
%_datadir/%name/*
%_datadir/pixmaps/*
%_datadir/gnome/apps/Applications/*
%_mandir/man1/*
%_menudir/%name


