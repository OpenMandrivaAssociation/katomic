Name:		katomic
Version:	20.03.80
Release:	1
Epoch:		1
Summary:	Build complex atoms with a minimal amount of moves
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=katomic
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5DBusAddons)

%description
KAtomic is a fun educational game built around molecular geometry.
It employs simplistic two-dimensional looks at different chemical elements.

%files -f katomic.lang
%{_sysconfdir}/xdg/katomic.knsrc
%{_bindir}/katomic
%{_datadir}/metainfo/org.kde.katomic.appdata.xml
%{_datadir}/applications/org.kde.katomic.desktop
%{_iconsdir}/hicolor/*/apps/katomic.png
%{_datadir}/katomic
%{_datadir}/kconf_update/katomic-levelset*
%{_datadir}/kxmlgui5/katomic/katomicui.rc
%{_datadir}/qlogging-categories5/katomic.categories

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang katomic --with-html
