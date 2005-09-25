
#
Summary:	Mount ISO image
Summary(pl):	Mount ISO image
Name:		mount-iso
Version:	0.9
Release:	0.1
License:	GPL
Group:		utils
Source0:	http://www.jinjiru.ru/files/mountiso/%{name}-%{version}.tar.bz2
# Source0-md5:	e2e126952c3a07c6a682bdb5b1f4ebc3
URL:		http://mountiso.jinjiru.ru/
#BuildRequires:	
#Requires:	
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mount ISO Image is an advanced script which allows to perform 
multiple operations with ISO, NRG (Nero Burning ROM), UDF (DVD),
CUE/BIN, CCD/IMG/SUB (CloneCD), XDVDFS (XBOX) images.

%description -l pl
-

%prep
%setup -q -n %{name}-image-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
