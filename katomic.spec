Name:		katomic
Version:	15.04.3
Release:	1
Epoch:		1
Summary:	Build complex atoms with a minimal amount of moves
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=katomic
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)

%description
KAtomic is a fun educational game built around molecular geometry.
It employs simplistic two-dimensional looks at different chemical elements.

%files
%{_kde_bindir}/katomic
%{_kde_applicationsdir}/katomic.desktop
%{_kde_docdir}/*/*/katomic
%{_kde_iconsdir}/hicolor/*/apps/katomic.png
%{_kde_appsdir}/katomic
%{_kde_configdir}/katomic.knsrc
%{_kde_appsdir}/kconf_update/katomic-levelset-upd.pl
%{_kde_appsdir}/kconf_update/katomic-levelset.upd

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

