function g(){const s=new URLSearchParams(window.location.search).get("sku"),n=document.getElementById("subjectInput");s&&n&&(n.value=`Quotation Request for Model ${s}`);const l=document.getElementById("vcOpenBtn"),d=document.getElementById("vcCloseBtn"),e=document.getElementById("vcDialog");l&&e&&l.addEventListener("click",()=>{e.showModal()}),d&&e&&d.addEventListener("click",()=>{e.close()}),e&&e.addEventListener("click",a=>{a.target===e&&e.close()});const c=document.getElementById("contactForm"),t=document.getElementById("formStatus");c&&t&&c.addEventListener("submit",a=>{a.preventDefault();const m=document.getElementById("nameInput"),u=document.getElementById("emailInput"),x=document.getElementById("phoneInput"),p=document.getElementById("commentInput"),i=m?.value.trim()||"",f=u?.value.trim()||"",v=x?.value.trim()||"",o=n?.value.trim()||"",r=p?.value.trim()||"",y=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;if(!i||i.length<2){t.innerHTML=`
            <div style="color: #991B1B; background: #FEF2F2; border: 1px solid #F87171; padding: 14px; border-radius: 4px; font-weight: 600; font-size: 14px;">
              <i class="fas fa-exclamation-triangle" aria-hidden="true"></i> Please provide your full name (minimum 2 characters).
            </div>
          `,m?.focus();return}if(!y.test(f)){t.innerHTML=`
            <div style="color: #991B1B; background: #FEF2F2; border: 1px solid #F87171; padding: 14px; border-radius: 4px; font-weight: 600; font-size: 14px;">
              <i class="fas fa-exclamation-triangle" aria-hidden="true"></i> Please enter a valid business email address.
            </div>
          `,u?.focus();return}if(!o||o.length<3){t.innerHTML=`
            <div style="color: #991B1B; background: #FEF2F2; border: 1px solid #F87171; padding: 14px; border-radius: 4px; font-weight: 600; font-size: 14px;">
              <i class="fas fa-exclamation-triangle" aria-hidden="true"></i> Please enter an inquiry subject or product SKU.
            </div>
          `,n?.focus();return}if(!r||r.length<5){t.innerHTML=`
            <div style="color: #991B1B; background: #FEF2F2; border: 1px solid #F87171; padding: 14px; border-radius: 4px; font-weight: 600; font-size: 14px;">
              <i class="fas fa-exclamation-triangle" aria-hidden="true"></i> Please provide details regarding your inquiry or requirements.
            </div>
          `,p?.focus();return}const h=`Name: ${i}
Email: ${f}
Phone: ${v||"N/A"}
Subject: ${o}

Message:
${r}

---
Dispatched via MAX GLOVES BD LTD. Exporter Portal`,b=`mailto:maxglovesbdltd@gmail.com?subject=${encodeURIComponent(`[RFQ Inquiry] ${o}`)}&body=${encodeURIComponent(h)}`;t.innerHTML=`
          <div style="background: #F8FAFC; border: 1px solid #CBD5E1; border-radius: 4px; padding: 24px; margin-top: 24px;">
            <div style="display: flex; align-items: flex-start; gap: 14px;">
              <i class="fas fa-info-circle text-crimson" style="font-size: 24px; margin-top: 2px;"></i>
              <div>
                <h4 style="color: #0B1118; font-size: 17px; font-weight: 700; margin: 0 0 6px;">
                  Inquiry Formatted for Direct Dispatch
                </h4>
                <p style="color: #334155; font-size: 14px; line-height: 1.6; margin: 0 0 16px;">
                  Thank you, <strong>${i}</strong>. Your inquiry has been validated and compiled. Click below to launch your email client to transmit it directly to our commercial sales desk at <strong>maxglovesbdltd@gmail.com</strong>, or call us immediately.
                </p>
                <div style="display: flex; flex-wrap: wrap; gap: 12px;">
                  <a href="${b}" class="btn-crimson font-mono" style="padding: 10px 20px; font-size: 13.5px;">
                    <i class="far fa-envelope"></i> Open in Email Client
                  </a>
                  <a href="https://wa.me/8801710591088" target="_blank" rel="noopener noreferrer" class="btn-steel-outline font-mono" style="padding: 10px 20px; font-size: 13.5px;">
                    <i class="fab fa-whatsapp" style="color: #25D366;"></i> WhatsApp +880 1710-591088
                  </a>
                </div>
              </div>
            </div>
          </div>
        `})}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();
