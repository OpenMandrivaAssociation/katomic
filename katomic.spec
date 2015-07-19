Name:		katomic
Version:	15.04.3
Release:	2
Epoch:		1
Summary:	Build complex atoms with a minimal amount of moves
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=katomic
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5NotifyConfig)

%description
KAtomic is a fun educational game built around molecular geometry.
It employs simplistic two-dimensional looks at different chemical elements.

%files
%doc %{_docdir}/HTML/*/katomic
%{_sysconfdir}/xdg/katomic.knsrc
%{_bindir}/katomic
%{_datadir}/appdata/katomic.appdata.xml
%{_datadir}/applications/org.kde.katomic.desktop
%{_iconsdir}/hicolor/*/apps/katomic.png
%{_datadir}/katomic
%{_datadir}/kconf_update/katomic-levelset-upd*
%{_datadir}/kxmlgui5/katomic/katomicui.rc

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

