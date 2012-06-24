# TODO: Name vs filename
Summary:	Mount ISO image
Summary(pl):	Program do montowania obraz�w p�yt
Name:		mount-iso
Version:	0.9
Release:	0.1
License:	GPL
Group:		utils
Source0:	http://www.jinjiru.ru/files/mountiso/%{name}-%{version}.tar.bz2
# Source0-md5:	e2e126952c3a07c6a682bdb5b1f4ebc3
URL:		http://mountiso.jinjiru.ru/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mount ISO Image is an advanced script which allows to perform multiple
operations with ISO, NRG (Nero Burning ROM), UDF (DVD), CUE/BIN,
CCD/IMG/SUB (CloneCD), XDVDFS (XBOX) images.

%description -l pl
Mount ISO Image jest zaawansowanym skryptem, kt�ry pozwala na
wykonywanie wielu operacji na plikach ISO, NRG (Nero Burning ROM), UDF
(DVD), CUE/BIN, CCD/IMG/SUB (CloneCD), XDVDFS (XBOX) b�d�cymi
obrazami p�yt.

%prep
%setup -q -n %{name}-image-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install install.sh	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/install.sh
