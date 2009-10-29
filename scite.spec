%define name 	scite
%define version 1.79
%define release %mkrel 4
%define libname %mklibname scintilla 0

%define scitever %(echo %{version} | sed -e 's/\\.//')

Summary: 	GTK text editor based on scintilla
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Editors
Url: 		http://www.scintilla.org/SciTE.html
Source: 	http://prdownloads.sourceforge.net/scintilla/scite%scitever.tgz
Source1:	scite.cmake
Requires:	%{libname} >= %version
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires: 	gtk+2-devel pkgconfig
BuildRequires:	desktop-file-utils
BuildRequires:	cmake >= 2.6
BuildRequires:	lua-devel >= 5.1
BuildRequires:	scintilla-devel >= 1.79

%description
SciTE is a GTK based single-document editor.  While its features are
limited, its main purpose is to show off scintilla, an extensible
text highlighting and formatting engine.

%prep
%setup -q -n scite
cp %SOURCE1 $RPM_BUILD_DIR/scite/CMakeLists.txt
rm -fr $RPM_BUILD_DIR/scintilla
perl -p -i -e 's/netscape/www-browser/g' src/Embedded.properties
perl -p -i -e 's/netscape/www-browser/g' src/SciTEGlobal.properties

%build
%{cmake}
%make

%install
rm -fr $RPM_BUILD_ROOT
cd build
%{makeinstall_std}

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-category='Application' \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc doc/*
%_bindir/SciTE
%_datadir/%name
%_datadir/pixmaps/*
%_datadir/applications/*
%_mandir/man1/*
